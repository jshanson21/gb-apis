import urllib.request, urllib.parse, urllib.error
import json
import gbobjects
import gbcontentfile as cf


# Returns the token stored in regToken.txt.  If no token is present,
# it returns None.
# This function will mainly be used by gbwiki.py to set the api_key
# before making API requests (instead of hard-coding the key in the file)
def getToken() :
    try : fh = open('regToken.txt', 'r')
    except : return None
    tmptext = fh.readline()
    return tmptext


#Initiates a parameters dictionary to be used for the urls that has the parameters
#that every function would use; is called by the functions below
def initParams() :
    params = dict()
    token = getToken()
    if token == None :
        print('===No Token Found===')
        return None
    params['api_key'] = token
    params['format'] = 'json'
    return params


#Passes in a dictionary with a set of filters and a dictionary with a set of parameters and adds the filters into the parameters dictionary.
def addFilters(filters, params) :
    params['filter'] = ''
    for field in filters :
        params['filter'] = params['filter'] + field + ':' + filters[field] + ','
    return params


#Takes in the url and list of parameters from the other functions below
# and retrives the data from the REST API response.  After doing error
# handling, the "results" object is taken out of the response
# and passed back
def loadData(url, params, errorMessage) :
    url = url + urllib.parse.urlencode(params)
    data = urllib.request.urlopen(url).read()
    try :
        jsdata = json.loads(data)
    except :
        jsdata = None
    if jsdata is None or jsdata["results"] == [] or "error" not in jsdata or jsdata["error"] != "OK" :
        print(errorMessage)
        return None
    return jsdata['results']


# Returns a list of generic GB objects for the supplied 
# The GB API calls return a small subset of the possible information for a
# "Get all X" call than they do for a "Get X" call (for example, you're
# going to get less information for Get Company than for Get Companies)
# You get so much less information that I decided the getXs calls would
# only send back the generic information that is attached to GBObjects.
def getGenericObjects(results) :
    tmplist = []
    for item in results :
        tmpitem = gbobjects.GBObject(item)
        tmplist.append(tmpitem)
    return tmplist


#Returns the json-formatted contents of a search; the query is in the format of
#a string
def search(query) :
    params = initParams()
    params['query'] = query
    return getMultipleResult('Search', params)

#Returns the json object containing all types; types are the classifications of content
#within the Giant Bomb wiki.  The "id" value is the 4-digit prefix found for each entry
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getTypes() :
    url = 'https://www.giantbomb.com/api/types/?'
    params = initParams()
    results = loadData(url, params, '===Could Not Retrieve Any Types===')
    tmplist = []
    for item in results :
        tmpitem = gbobjects.Type(item)
        tmplist.append(tmpitem)
    return tmplist  



# Takes in a keyword and key for the type of function to be run and then returns the results
# The logic for getting and creating GBObjects generally was exactly the same for
# each element in the wiki other than things like the URL and Key.  This function
# helps standardize the way in which the information is obtained so that it is easier 
# to make updates to one function instead of 20 or so
def getSingleResult(gbType, key) :
    url = cf.getSingleBaseUrl(gbType)
    if url == None : return None
    url = url + key + '/?'
    params = initParams()
    errorMessage = cf.getSingleErrorMessage(gbType)
    results = loadData(url, params, errorMessage)
    if results is None : return results
    if gbType == 'Accessory' : return gbobjects.Accessory(results)
    elif gbType == 'Character' : return gbobjects.Character(results)
    elif gbType == 'Company' : return gbobjects.Company(results)
    elif gbType == 'Concept' : return gbobjects.Concept(results)
    elif gbType == 'DLC' : return gbobjects.Dlc(results)
    elif gbType == 'Franchise' : return gbobjects.Franchise(results)
    elif gbType == 'Game' : return gbobjects.Game(results)
    elif gbType == 'GameRating' : return gbobjects.GameRating(results)
    elif gbType == 'Genre' : return gbobjects.Genre(results)
    elif gbType == 'Location' : return gbobjects.Location(results)
    elif gbType == 'Object' : return gbobjects.Object(results)
    elif gbType == 'Person' : return gbobjects.Person(results)
    elif gbType == 'Platform' : return gbobjects.Platform(results)
    elif gbType == 'Promo' : return gbobjects.Promo(results)
    elif gbType == 'RatingBoard' : return gbobjects.RatingBoard(results)
    elif gbType == 'Region' : return gbobjects.Region(results)
    elif gbType == 'Release' : return gbobjects.Release(results)
    elif gbType == 'Review' : return gbobjects.Review(results)
    elif gbType == 'Theme' : return gbobjects.Theme(results)
    elif gbType == 'UserReview' : return gbobjects.UserReview(results)
    else :
        print("gbType not recognized")
        return None




# Takes in a keyword and key for the type of function to be run and then returns the results
# The logic for getting and creating GBObjects generally was exactly the same for
# each element in the wiki other than things like the URL and Key.  This function
# helps standardize the way in which the information is obtained so that it is easier 
# to make updates to one function instead of 20 or so
def getMultipleResult(gbType, filters) :
    url = cf.getMultipleBaseUrl(gbType)
    if url == None : return None
    params = initParams()
    if gbType == 'Search' : params['query'] = filters['query']
    else : params = addFilters(filters, params)
    errorMessage = cf.getMultipleErrorMessage(gbType)
    results = loadData(url, params, errorMessage)
    if results is None : return results
# GameRatings have fewer generic items than do the other objects
# GameRatings is thus the only object that does not inherit from GBObject, so it
# needs special handling here
    if gbType == 'GameRatings' : 
        tmplist = []
        for item in results :
            tmpitem = gbobjects.GameRating(item)
            tmplist.append(tmpitem)
        return tmplist
# Region also has fewer generic items than the other objects, so it also does not inherit
# from GBObject
    elif gbType == 'Regions' : 
        tmplist = []
        for item in results :
            tmpitem = gbobjects.Region(item)
            tmplist.append(tmpitem)
        return tmplist
# Review also falls into this category
    elif gbType == 'Reviews' : 
        tmplist = []
        for item in results :
            tmpitem = gbobjects.Review(item)
            tmplist.append(tmpitem)
        return tmplist  
# As does Theme
    elif gbType == 'Themes' : 
        tmplist = []
        for item in results :
            tmpitem = gbobjects.Theme(item)
            tmplist.append(tmpitem)
        return tmplist    
# And UserReview
    elif gbType == 'UserReviews' : 
        tmplist = []
        for item in results :
            tmpitem = gbobjects.UserReview(item)
            tmplist.append(tmpitem)
        return tmplist    
# and Search
    elif gbType == 'Search' :
        tmplist = []
        for item in results :
            tmpitem = gbobjects.SearchObject(item)
            tmplist.append(tmpitem)
        return tmplist           
# Handling for all other object types
    else :
        return getGenericObjects(results)



#Returns an Accessory object for an accessory in the wiki based on the key (a string)
def getAccessory(key) :
    return getSingleResult('Accessory', key)


#Returns a list of GB objects that match the Accessory filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getAccessories(filters) :
    return getMultipleResult('Accessories', filters)


#Returns the a Character object for a character in the wiki based on the key (a string)
def getCharacter(key) :
    return getSingleResult('Character', key)

#Returns a list of GB Objects that match the Character filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getCharacters(filters) :
    return getMultipleResult('Characters', filters)


#Returns a company in the wiki based on the key (a string)
def getCompany(key) :
    return getSingleResult('Company', key)

#Returns a list of GBobjects containing all companies that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getCompanies(filters) :
    return getMultipleResult('Companies', filters)


#Returns a concept in the wiki based on the key (a string)
def getConcept(key) :
    return getSingleResult('Concept', key)

#Returns a list of GBobjects containing all concepts that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getConcepts(filters) :
    return getMultipleResult('Concepts', filters)


#Returns a DLC in the wiki based on the key (a string)
def getDLC(key) :
    return getSingleResult('DLC', key)

#Returns a list of GBobjects containing all DLCs that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getDLCs(filters) :
    return getMultipleResult('DLCs', filters)


#Returns a franchise in the wiki based on the key (a string)
def getFranchise(key) :
    return getSingleResult('Franchise', key)

#Returns a list of GBobjects containing all franchises that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getFranchises(filters) :
    return getMultipleResult('Franchises', filters)


#Returns a game in the wiki based on the key (a string)
def getGame(key) :
    return getSingleResult('Game', key)

#Returns a list of GBobjects containing all games that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getGames(filters) :
    return getMultipleResult('Games', filters)


#Returns a game rating (like the ESRB's E10) in the wiki
#based on the key (a string)
def getGameRating(key) :
    return getSingleResult('GameRating', key)

#Returns a list of GBobjects containing all game ratings that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
#This function does not use the Generic Objects function
#because GameRating does not inherit from GBObject
def getGameRatings(filters) :
    return getMultipleResult('GameRatings', filters)


#Returns a genre in the wiki based on the key (a string)
def getGenre(key) :
    return getSingleResult('Genre', key)

#Returns a list of GBobjects containing all genres that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getGenres(filters) :
    return getMultipleResult('Genres', filters)


#Returns an location in the wiki based on the key (a string)
def getLocation(key) :
    return getSingleResult('Location', key)

#Returns a list of GBobjects containing all locations that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getLocations(filters) :
    return getMultipleResult('Locations', filters)


#Returns an object (like an item or a power-up) in the wiki
#based on the key (a string)
def getObject(key) :
    return getSingleResult('Object', key)

#Returns a list of gbobjects containing all objects that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getObjects(filters) :
    return getMultipleResult('Objects', filters)


#Returns a person in the wiki based on the key (a string)
def getPerson(key) :
    return getSingleResult('Person', key)

#Returns a list of gbobjects containing all people that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getPeople(filters) :
    return getMultipleResult('People', filters)


#Returns a platform (e.g., PS5) in the wiki based on the key (a string)
def getPlatform(key) :
    return getSingleResult('Platform', key)

#Returns a list of GBobjects containing all platforms that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getPlatforms(filters) :
    return getMultipleResult('Platforms', filters)


#Returns a promo in the wiki based on the key (a string)
def getPromo(key) :
    return getSingleResult('Promo', key)

#Returns a list of GBobjects containing all promos that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getPromos(filters) :
    return getMultipleResult('Promos', filters)


#Returns the json object for a rating board (like ESRB) in the wiki based
#on the key (a string)
def getRatingBoard(key) :
    return getSingleResult('RatingBoard', key)

#Returns the json object containing all rating boards that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getRatingBoards(filters) :
    return getMultipleResult('RatingBoards', filters)

#Returns the json object for a region in the wiki based on the key (a string)
def getRegion(key) :
    return getSingleResult('Region', key)

#Returns the json object containing all regions that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getRegions(filters) :
    return getMultipleResult('Regions', filters)


#Returns the json object for a release in the wiki based on the key (a string)
def getRelease(key) :
    return getSingleResult('Release', key)

#Returns the json object containing all releases that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getReleases(filters) :
    return getMultipleResult('Releases', filters)


#Returns the json object for a review in the wiki based on the key (a string)
def getReview(key) :
    return getSingleResult('Review', key)

#Returns the json object containing all reviews that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getReviews(filters) :
    return getMultipleResult('Reviews', filters)


#Returns the json object for a theme in the wiki based on the key (a string)
def getTheme(key) :
    return getSingleResult('Theme', key)

#Returns the json object containing all themes that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getThemes(filters) :
    return getMultipleResult('Themes', filters)


#Returns the json object for a user review in the wiki based on the key (a string)
def getUserReview(key) :
    return getSingleResult('UserReview', key)

#Returns the json object containing all user reviews that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getUserReviews(filters) :
    return getMultipleResult('UserReviews', filters)

