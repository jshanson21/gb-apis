import urllib.request, urllib.parse, urllib.error
import json

#Initiates a parameters dictionary to be used for the urls that has the parameters
#that every function would use; is called by the functions below
#THE API_KEY NEEDS TO BE UPDATED WITH YOUR API KEY
def initParams() :
    params = dict()
    params['api_key'] = '6da2f5489cc2a154ca0ea4b461b0376d49d442a4'
    params['format'] = 'json'
    return(params)

#Passes in a dictionary with a set of filters and a dictionary with a set of parameters and adds the filters into the parameters dictionary.
def addFilters(filters, params) :
    params['filter'] = ''
    for field in filters :
        params['filter'] = params['filter'] + field + ':' + filters[field] + ','
    return params

#Takes in the url and list of parameters from the other functions below and
#retrives the data from the REST API response.  The entire JSON object is returned
#as an object.
def loadData(url, params, errorMessage) :
    url = url + urllib.parse.urlencode(params)
    print(url)
    data = urllib.request.urlopen(url).read()
    try :
        jsdata = json.loads(data)
    except :
        jsdata = None
    if jsdata is None or jsdata["results"] == [] or "error" not in jsdata or jsdata["error"] != "OK" :
        print(errorMessage)
    return jsdata


#Given a 6-digit MYAPP code, returns the regToken.  The regToken is used in place
#of the api-key in API requests
def authorizeUser(code) :
    url = 'http://www.giantbomb.com/app/myapp/get-result?'
    params = dict()
    params['regCode'] = code
    params['format'] = json
    url = url + urllib.parse.urlencode(params)
    data = urllib.request.urlopen(url).read()
    try :
        jsdata = json.loads(data)
    except :
        jsdata = None
    if jsdata is None or jsdata["status"] != "success" :
        print('===Could not get regToken===')
        return None
    return jsdata["regToken"]


#Returns the json object for an accessory in the wiki based on the key (a string)
def getAccessory(key) :
    url = 'https://www.giantbomb.com/api/accessory/' + key + '/?'
    params = initParams()
    return loadData(url, params, '===Could Not Retrieve Accessory===')

#Returns the json object containing all accessories that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getAccessories(filters) :
    url = 'https://www.giantbomb.com/api/accessories/?'
    params = initParams()
    params = addFilters(filters, params)
    return loadData(url, params, '===Could Not Retrieve Any Accessories===')

#Returns the json object for a character in the wiki based on the key (a string)
def getCharacter(key) :
    url = 'https://www.giantbomb.com/api/character/' + key + '/?'
    params = initParams()
    return loadData(url, params, '===Could Not Retrieve Character===')

#Returns the json object containing all characters that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getCharacters(filters) :
    url = 'https://www.giantbomb.com/api/characters/?'
    params = initParams()
    params = addFilters(filters, params)
    return loadData(url, params, '===Could Not Retrieve Any Characters===')


#Returns the json object for a chat that is connected with a Giant Bomb Twitch stream; the chat is based on the key (a string)
def getChat(key) :
    url = 'https://www.giantbomb.com/api/chat/' + key + '/?'
    params = initParams()
    return loadData(url, params, '===Could Not Retrieve Chat===')


#Returns the json object containing all chats that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getChats(filters) :
    url = 'https://www.giantbomb.com/api/chats/?'
    params = initParams()
    params = addFilters(filters, params)
    return loadData(url, params, '===Could Not Retrieve Any Chats===')

#Returns the json object for a company in the wiki based on the key (a string)
def getCompany(key) :
    url = 'https://www.giantbomb.com/api/company/' + key + '/?'
    params = initParams()
    return loadData(url, params, '===Could Not Retrieve Company===')

#Returns the json object containing all companies that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getCompanies(filters) :
    url = 'https://www.giantbomb.com/api/companies/?'
    params = initParams()
    params = addFilters(filters, params)
    return loadData(url, params, '===Could Not Retrieve Any Companies===')


#Returns the json object for a concept in the wiki based on the key (a string)
def getConcept(key) :
    url = 'https://www.giantbomb.com/api/concept/' + key + '/?'
    params = initParams()
    return loadData(url, params, '===Could Not Retrieve Concept===')

#Returns the json object containing all concepts that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getConcepts(filters) :
    url = 'https://www.giantbomb.com/api/concepts/?'
    params = initParams()
    params = addFilters(filters, params)
    return loadData(url, params, '===Could Not Retrieve Any Concepts===')


#Returns the json object for a DLC in the wiki based on the key (a string)
def getDLC(key) :
    url = 'https://www.giantbomb.com/api/dlc/' + key + '/?'
    params = initParams()
    return loadData(url, params, '===Could Not Retrieve DLC===')

#Returns the json object containing all DLCs that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getDLCs(filters) :
    url = 'https://www.giantbomb.com/api/dlcs/?'
    params = initParams()
    params = addFilters(filters, params)
    return loadData(url, params, '===Could Not Retrieve Any DLCs===')


#Returns the json object for a franchise in the wiki based on the key (a string)
def getFranchise(key) :
    url = 'https://www.giantbomb.com/api/franchise/' + key + '/?'
    params = initParams()
    return loadData(url, params, '===Could Not Retrieve Franchise===')

#Returns the json object containing all franchises that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getFranchises(filters) :
    url = 'https://www.giantbomb.com/api/franchises/?'
    params = initParams()
    params = addFilters(filters, params)
    return loadData(url, params, '===Could Not Retrieve Any Franchises===')


#Returns the json object for a game in the wiki based on the key (a string)
def getGame(key) :
    url = 'https://www.giantbomb.com/api/game/' + key + '/?'
    params = initParams()
    return loadData(url, params, '===Could Not Retrieve Game===')

#Returns the json object containing all games that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getGames(filters) :
    url = 'https://www.giantbomb.com/api/games/?'
    params = initParams()
    params = addFilters(filters, params)
    return loadData(url, params, '===Could Not Retrieve Any Games===')


#Returns the json object for a game rating (like the ESRB's E10) in the wiki
#based on the key (a string)
def getGameRating(key) :
    url = 'https://www.giantbomb.com/api/game_rating/' + key + '/?'
    params = initParams()
    return loadData(url, params, '===Could Not Retrieve Game Rating===')

#Returns the json object containing all game ratings that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getGameRatings(filters) :
    url = 'https://www.giantbomb.com/api/game_ratings/?'
    params = initParams()
    params = addFilters(filters, params)
    return loadData(url, params, '===Could Not Retrieve Any Game Ratings===')


#Returns the json object for a genre in the wiki based on the key (a string)
def getGenre(key) :
    url = 'https://www.giantbomb.com/api/genre/' + key + '/?'
    params = initParams()
    return loadData(url, params, '===Could Not Retrieve Genre===')

#Returns the json object containing all genres that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getGenres(filters) :
    url = 'https://www.giantbomb.com/api/genres/?'
    params = initParams()
    params = addFilters(filters, params)
    return loadData(url, params, '===Could Not Retrieve Any Genres===')


#Returns the json object for an image in the wiki based on the key (a string)
#This is commented out for now, as I'm not quire sure how to use it Since
#I can't really find examples of it within the wiki.  I'm also not sure of the
#usage because games, etc. return their own image URLs
#def getImage(key) :
#    url = 'https://www.giantbomb.com/api/images/' + key + '/?'
#    params = initParams()
#    return loadData(url, params, '===Could Not Retrieve Image===')



#Returns the json object for a location in the wiki based on the key (a string)
def getLocation(key) :
    url = 'https://www.giantbomb.com/api/location/' + key + '/?'
    params = initParams()
    return loadData(url, params, '===Could Not Retrieve Location===')

#Returns the json object containing all locations that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getLocations(filters) :
    url = 'https://www.giantbomb.com/api/locations/?'
    params = initParams()
    params = addFilters(filters, params)
    return loadData(url, params, '===Could Not Retrieve Any Locations===')


#Returns the json object for an object (like an item or a power-up) in the wiki
#based on the key (a string)
def getObject(key) :
    url = 'https://www.giantbomb.com/api/object/' + key + '/?'
    params = initParams()
    return loadData(url, params, '===Could Not Retrieve Object===')

#Returns the json object containing all objects that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getObjects(filters) :
    url = 'https://www.giantbomb.com/api/objects/?'
    params = initParams()
    params = addFilters(filters, params)
    return loadData(url, params, '===Could Not Retrieve Any Objects===')


#Returns the json object for a person in the wiki based on the key (a string)
def getPerson(key) :
    url = 'https://www.giantbomb.com/api/person/' + key + '/?'
    params = initParams()
    return loadData(url, params, '===Could Not Retrieve Person===')

#Returns the json object containing all people that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getPeople(filters) :
    url = 'https://www.giantbomb.com/api/people/?'
    params = initParams()
    params = addFilters(filters, params)
    return loadData(url, params, '===Could Not Retrieve Any People===')


#Returns the json object for a platform (e.g., PS5) in the wiki based
#on the key (a string)
def getPlatform(key) :
    url = 'https://www.giantbomb.com/api/platform/' + key + '/?'
    params = initParams()
    return loadData(url, params, '===Could Not Retrieve Platform===')

#Returns the json object containing all platforms that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getPlatforms(filters) :
    url = 'https://www.giantbomb.com/api/platforms/?'
    params = initParams()
    params = addFilters(filters, params)
    return loadData(url, params, '===Could Not Retrieve Any Platforms===')


#Returns the json object for a promo in the wiki based on the key (a string)
def getPromo(key) :
    url = 'https://www.giantbomb.com/api/promo/' + key + '/?'
    params = initParams()
    return loadData(url, params, '===Could Not Retrieve Promo===')

#Returns the json object containing all promos that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getPromos(filters) :
    url = 'https://www.giantbomb.com/api/promos/?'
    params = initParams()
    params = addFilters(filters, params)
    return loadData(url, params, '===Could Not Retrieve Any Promos===')


#Returns the json object for a rating board (like ESRB) in the wiki based
#on the key (a string)
def getRatingBoard(key) :
    url = 'https://www.giantbomb.com/api/rating_board/' + key + '/?'
    params = initParams()
    return loadData(url, params, '===Could Not Retrieve Rating Board===')

#Returns the json object containing all rating boards that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getRatingBoards(filters) :
    url = 'https://www.giantbomb.com/api/rating_boards/?'
    params = initParams()
    params = addFilters(filters, params)
    return loadData(url, params, '===Could Not Retrieve Any Rating Boards===')



#Returns the json object for a region in the wiki based on the key (a string)
def getRegion(key) :
    url = 'https://www.giantbomb.com/api/region/' + key + '/?'
    params = initParams()
    return loadData(url, params, '===Could Not Retrieve Region===')

#Returns the json object containing all regions that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getRegions(filters) :
    url = 'https://www.giantbomb.com/api/regions/?'
    params = initParams()
    params = addFilters(filters, params)
    return loadData(url, params, '===Could Not Retrieve Any Regions===')


#Returns the json object for a release in the wiki based on the key (a string)
def getRelease(key) :
    url = 'https://www.giantbomb.com/api/release/' + key + '/?'
    params = initParams()
    return loadData(url, params, '===Could Not Retrieve Release===')

#Returns the json object containing all releases that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getReleases(filters) :
    url = 'https://www.giantbomb.com/api/releases/?'
    params = initParams()
    params = addFilters(filters, params)
    return loadData(url, params, '===Could Not Retrieve Any Releases===')


#Returns the json object for a review in the wiki based on the key (a string)
def getReview(key) :
    url = 'https://www.giantbomb.com/api/review/' + key + '/?'
    params = initParams()
    return loadData(url, params, '===Could Not Retrieve Review===')

#Returns the json object containing all reviews that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getReviews(filters) :
    url = 'https://www.giantbomb.com/api/reviews/?'
    params = initParams()
    params = addFilters(filters, params)
    return loadData(url, params, '===Could Not Retrieve Any Reviews===')


#Returns the json-formatted contents of a search; the query is in the format of
#a string
def search(query) :
    url = 'https://www.giantbomb.com/api/search/?'
    params = initParams()
    params['query'] = query
    return loadData(url, params, '===Search error or no results found===')


#Returns the json object for a theme in the wiki based on the key (a string)
def getTheme(key) :
    url = 'https://www.giantbomb.com/api/theme/' + key + '/?'
    params = initParams()
    return loadData(url, params, '===Could Not Retrieve Theme===')

#Returns the json object containing all themes that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getThemes(filters) :
    url = 'https://www.giantbomb.com/api/themes/?'
    params = initParams()
    params = addFilters(filters, params)
    return loadData(url, params, '===Could Not Retrieve Any Themes===')

#Returns the json object containing all types; types are the classifications of content
#within the Giant Bomb wiki.  The "id" value is the 4-digit prefix found for each entry
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getTypes(filters) :
    url = 'https://www.giantbomb.com/api/types/?'
    params = initParams()
    params = addFilters(filters, params)
    return loadData(url, params, '===Could Not Retrieve Any Types===')


#Returns the json object for a user review in the wiki based on the key (a string)
def getUserReview(key) :
    url = 'https://www.giantbomb.com/api/user_review/' + key + '/?'
    params = initParams()
    return loadData(url, params, '===Could Not Retrieve User Review===')

#Returns the json object containing all user reviews that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getUserReviews(filters) :
    url = 'https://www.giantbomb.com/api/user_reviews/?'
    params = initParams()
    params = addFilters(filters, params)
    return loadData(url, params, '===Could Not Retrieve Any User Reviews===')


#Returns the json object for a Giant Bomb video in the wiki based on the key (a string)
def getVideo(key) :
    url = 'https://www.giantbomb.com/api/video/' + key + '/?'
    params = initParams()
    return loadData(url, params, '===Could Not Retrieve Video===')

#Returns the json object containing all GB videos that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getVideos(filters) :
    url = 'https://www.giantbomb.com/api/videos/?'
    params = initParams()
    params = addFilters(filters, params)
    return loadData(url, params, '===Could Not Retrieve Any Videos===')


#Returns the json object for a video category in the wiki based on the key (a string)
def getVideoCategory(key) :
    url = 'https://www.giantbomb.com/api/video_category/' + key + '/?'
    params = initParams()
    return loadData(url, params, '===Could Not Retrieve Video Category===')

#Returns the json object containing all video categories that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getVideoCategories(filters) :
    url = 'https://www.giantbomb.com/api/video_categories/?'
    params = initParams()
    params = addFilters(filters, params)
    return loadData(url, params, '===Could Not Retrieve Any Video Categories===')


#Returns the json object for a video show (the names of specific types of shows,
#like "Mario Madness") in the wiki based on the key (a string)
def getVideoShow(key) :
    url = 'https://www.giantbomb.com/api/video_show/' + key + '/?'
    params = initParams()
    return loadData(url, params, '===Could Not Retrieve Video Category===')

#Returns the json object containing all video shows that match the filter criteria
#The function takes in a dictionary with each pair consisting of ["field":"value"]
def getVideoShows(filters) :
    url = 'https://www.giantbomb.com/api/video_shows/?'
    params = initParams()
    params = addFilters(filters, params)
    return loadData(url, params, '===Could Not Retrieve Any Video Shows===')


#Returns the json object containing all live streams that are currently running.
def getCurrentLive() :
    url = 'https://www.giantbomb.com/api/video/current-live/?'
    params = initParams()
    url = url + urllib.parse.urlencode(params)
    data = urllib.request.urlopen(url).read()
    try :
        jsdata = json.loads(data)
    except :
        jsdata = None
    if jsdata is None or jsdata["success"] != 1 or jsdata["video"] is None:
        print('===No Live Shows Running Now===')
    return jsdata


#Returns the json object containing the saved pause time of the given video for the
#user with the given API key.  This endpoint MUST have a video_id, which is input
#as just a string
def getSavedTime(vid_id) :
    url = 'https://www.giantbomb.com/api/video/get-saved-time/?'
    params = initParams()
    params['video_id'] = vid_id
    url = url + urllib.parse.urlencode(params)
    data = urllib.request.urlopen(url).read()
    try :
        jsdata = json.loads(data)
    except :
        jsdata = None
    if jsdata is None or jsdata["savedTime"] == [] or jsdata["success"] != 1 :
        print('===Could Not Retrieve Saved Time===')
    return jsdata

#Saves the pause time for the given user for the given video ID.  The parameters
#are both strings
def saveTime(vid_id, saveTime) :
    url = 'https://www.giantbomb.com/api/video/save-time/?'
    params = initParams()
    params['video_id'] = vid_id
    params['time_to_save'] = saveTime
    url = url + urllib.parse.urlencode(params)
    data = urllib.request.urlopen(url).read()
    try :
        jsdata = json.loads(data)
    except :
        jsdata = None
    if jsdata is None or jsdata["success"] != 1 :
        print('===Could Not Save Time===')
    else :
        print('Time saved successfully.')

#Returns the json object containing all saved video times for the API user.
#The loadData steps are here because the error handling for this call is different
#from the rest
def getAllSavedTimes() :
    url = 'https://www.giantbomb.com/api/video/get-all-saved-times/?'
    params = initParams()
    url = url + urllib.parse.urlencode(params)
    data = urllib.request.urlopen(url).read()
    try :
        jsdata = json.loads(data)
    except :
        jsdata = None
    if jsdata is None or jsdata["savedTimes"] == [] or jsdata["success"] != 1 :
        print('===No Saved Times for this User===')
    return jsdata
