import gbwiki

# Checks to see if the user wanted to automatically skip through all of the tests without
# manual intervention or to need to press a key before each test goes
def autoChk() :
    if manual_run == "y" :
        input("Press Enter to continue")
    else :
        return

def runSingleTest(gbType, key) :
    if gbType == 'Accessory' : tmp = gbwiki.getAccessory(key)
    elif gbType == 'Character' : tmp = gbwiki.getCharacter(key)
    elif gbType == 'Company' : tmp = gbwiki.getCompany(key)
    elif gbType == 'Concept' : tmp = gbwiki.getConcept(key)
    elif gbType == 'DLC' : tmp = gbwiki.getDLC(key)
    elif gbType == 'Franchise' : tmp = gbwiki.getFranchise(key)
    elif gbType == 'Game' : tmp = gbwiki.getGame(key)
    elif gbType == 'GameRating' : tmp = gbwiki.getGameRating(key)
    elif gbType == 'Genre' : tmp = gbwiki.getGenre(key)
    elif gbType == 'Location' : tmp = gbwiki.getLocation(key)
    elif gbType == 'Object' : tmp = gbwiki.getObject(key)
    elif gbType == 'Person' : tmp = gbwiki.getPerson(key)
    elif gbType == 'Platform' : tmp = gbwiki.getPlatform(key)
    elif gbType == 'Promo' : tmp = gbwiki.getPromo(key)
    elif gbType == 'RatingBoard' : tmp = gbwiki.getRatingBoard(key)
    elif gbType == 'Region' : tmp = gbwiki.getRegion(key)
    elif gbType == 'Release' : tmp = gbwiki.getRelease(key)
    elif gbType == 'Review' : tmp = gbwiki.getReview(key)
    elif gbType == 'Theme' : tmp = gbwiki.getTheme(key)
    elif gbType == 'UserReview' : tmp = gbwiki.getUserReview(key)
    else :
        print("gbType not recognized")
        return   
# Checking to see if the API call returned nothing or had an error; most of the keys
# in this test should work, but Promos do not run all the time.  This test is 
# mainly to prevent a lack of promos from breaking the test
    if tmp == None : return
# Prints off the attributes common to all objects except those which do not
# inherit from GBObject
    if gbType not in ['GameRating', 'Region', 'Review', 'Theme', 'UserReview'] :
        print(tmp.api_detail_url)
        print(tmp.date_added)
        print(tmp.date_last_updated)
        print(tmp.deck)
        print(tmp.description)
        print(tmp.guid)
        print(tmp.id)
        print(tmp.image_urls)
        print(tmp.name)
        print(tmp.site_detail_url) 
    if gbType == 'Accessory' : 
        print(tmp.image_tags)
    elif gbType == 'Character' : 
        print(tmp.aliases)
        print(tmp.birthday)
        print(tmp.concepts)
        print(tmp.enemies)
        print(tmp.first_appeared_in_game)
        print(tmp.franchises)
        print(tmp.friends)
        print(tmp.games)
        print(tmp.gender)
        print(tmp.image_tags)
        print(tmp.last_name)
        print(tmp.locations)
        print(tmp.objects)
        print(tmp.people)
        print(tmp.real_name)
    elif gbType == 'Company' : 
        print(tmp.abbreviation)
        print(tmp.aliases)
        print(tmp.characters)
        print(tmp.concepts)
        print(tmp.date_founded)
        print(tmp.developed_games)
        print(tmp.developer_releases)
        print(tmp.distributor_releases)
        print(tmp.image_tags)
        print(tmp.location_address)
        print(tmp.location_city)
        print(tmp.location_country)
        print(tmp.location_state)
        print(tmp.locations)
        print(tmp.objects)
        print(tmp.people)
        print(tmp.phone)
        print(tmp.published_games)
        print(tmp.publisher_releases)
        print(tmp.website)
    elif gbType == 'Concept' : 
        print(tmp.aliases)
        print(tmp.characters)
        print(tmp.concepts)
        print(tmp.first_appeared_in_franchise)
        print(tmp.first_appeared_in_game)
        print(tmp.franchises)
        print(tmp.games)
        print(tmp.image_tags)
        print(tmp.locations)
        print(tmp.objects)
        print(tmp.people)
        print(tmp.related_concepts)
    elif gbType == 'DLC' : 
        print(tmp.game)
        print(tmp.platform)
        print(tmp.release_date)
    elif gbType == 'Franchise' : 
        print(tmp.aliases)
        print(tmp.characters)
        print(tmp.concepts)
        print(tmp.games)
        print(tmp.image_tags)
        print(tmp.locations)
        print(tmp.objects)
        print(tmp.people)
    elif gbType == 'Game' : 
        print(tmp.aliases)
        print(tmp.characters)
        print(tmp.concepts)
        print(tmp.developers)
        print(tmp.expected_release_day)
        print(tmp.expected_release_month)
        print(tmp.expected_release_quarter)
        print(tmp.expected_release_year)
        print(tmp.first_appearance_characters)
        print(tmp.first_appearance_concepts)
        print(tmp.first_appearance_locations)
        print(tmp.first_appearance_objects)
        print(tmp.first_appearance_people)
        print(tmp.franchises)
        print(tmp.genres)
        print(tmp.images)
        print(tmp.image_tags)
        print(tmp.killed_characters)
        print(tmp.locations)
        print(tmp.number_of_user_reviews)
        print(tmp.objects)
        print(tmp.original_game_rating)
        print(tmp.original_release_date)
        print(tmp.people)
        print(tmp.platforms)
        print(tmp.publishers)
        print(tmp.releases)
        print(tmp.dlcs)
        print(tmp.reviews)
        print(tmp.similar_games)
        print(tmp.themes)
        print(tmp.videos)
    elif gbType == 'GameRating' : 
        print(tmp.api_detail_url)
        print(tmp.guid)
        print(tmp.id)
        print(tmp.image_urls)
        print(tmp.name)
        print(tmp.rating_board)
    elif gbType == 'Genre' : 
        print("No Genre-specific fields")
    elif gbType == 'Location' : 
        print(tmp.aliases)
        print(tmp.first_appeared_in_game)
        print(tmp.image_tags)
    elif gbType == 'Object' : 
        print(tmp.aliases)
        print(tmp.characters)
        print(tmp.companies)
        print(tmp.concepts)
        print(tmp.first_appeared_in_game)
        print(tmp.franchises)
        print(tmp.games)
        print(tmp.image_tags)
        print(tmp.locations)
        print(tmp.objects)
        print(tmp.people)
    elif gbType == 'Person' : 
        print(tmp.aliases)
        print(tmp.birth_date)
        print(tmp.characters)
        print(tmp.concepts)
        print(tmp.country)
        print(tmp.death_date)
        print(tmp.first_credited_game)
        print(tmp.franchises)
        print(tmp.games)
        print(tmp.gender)
        print(tmp.hometown)
        print(tmp.image_tags)
        print(tmp.locations)
        print(tmp.objects)
        print(tmp.people)
    elif gbType == 'Platform' : 
        print(tmp.abbreviation)
        print(tmp.company)
        print(tmp.image_tags)
        print(tmp.install_base)
        print(tmp.online_support)
        print(tmp.original_price)
        print(tmp.release_date)
    elif gbType == 'Promo' : 
        print(tmp.link)
        print(tmp.resource_type)
        print(tmp.user)
    elif gbType == 'RatingBoard' : 
        print(tmp.region)
    elif gbType == 'Region' : 
        print(tmp.api_detail_url)
        print(tmp.date_added)
        print(tmp.date_last_updated)
        print(tmp.deck)
        print(tmp.description)
        print(tmp.guid)
        print(tmp.id)
        print(tmp.image_urls)
        print(tmp.name)
        print(tmp.rating_boards)
    elif gbType == 'Release' : 
        print(tmp.developers)
        print(tmp.expected_release_day)
        print(tmp.expected_release_month)
        print(tmp.expected_release_quarter)
        print(tmp.expected_release_year)
        print(tmp.game)
        print(tmp.game_rating)
        print(tmp.maximum_players)
        print(tmp.minimum_players)
        print(tmp.multiplayer_features)
        print(tmp.platform)
        print(tmp.product_code_type)
        print(tmp.product_code_value)
        print(tmp.publishers)
        print(tmp.region)
        print(tmp.release_date)
        print(tmp.resolutions)
        print(tmp.singleplayer_features)
        print(tmp.sound_systems)
        print(tmp.widescreen_support)
    elif gbType == 'Review' : 
        print(tmp.api_detail_url)
        print(tmp.deck)
        print(tmp.description)
        print(tmp.dlc_name)
        print(tmp.game)
        print(tmp.guid)
        print(tmp.id)
        print(tmp.platforms)
        print(tmp.publish_date)
        print(tmp.release)
        print(tmp.reviewer)
        print(tmp.score)
        print(tmp.site_detail_url)
    elif gbType == 'Theme' : 
        print(tmp.api_detail_url)
        print(tmp.guid)
        print(tmp.id)
        print(tmp.name)
        print(tmp.site_detail_url)
    elif gbType == 'UserReview' :
        print(tmp.api_detail_url)
        print(tmp.date_added)
        print(tmp.date_last_updated)
        print(tmp.deck)
        print(tmp.description)
        print(tmp.game)
        print(tmp.release)
        print(tmp.dlc)
        print(tmp.guid)
        print(tmp.id)
        print(tmp.reviewer)
        print(tmp.score)
        print(tmp.site_detail_url)
    else :
        print("gbType not recognized")
        return  
    print("\n")
    return


def runMultipleTest(gbType, filters) :
    if gbType == 'Accessories' : tmp = gbwiki.getAccessories(filters)
    elif gbType == 'Characters' : tmp = gbwiki.getCharacters(filters)
    elif gbType == 'Companies' : tmp = gbwiki.getCompanies(filters)
    elif gbType == 'Concepts' : tmp = gbwiki.getConcepts(filters)
    elif gbType == 'DLCs' : tmp = gbwiki.getDLCs(filters)
    elif gbType == 'Franchises' : tmp = gbwiki.getFranchises(filters)
    elif gbType == 'Games' : tmp = gbwiki.getGames(filters)
    elif gbType == 'GameRatings' : tmp = gbwiki.getGameRatings(filters)
    elif gbType == 'Genres' : tmp = gbwiki.getGenres(filters)
    elif gbType == 'Locations' : tmp = gbwiki.getLocations(filters)
    elif gbType == 'Objects' : tmp = gbwiki.getObjects(filters)
    elif gbType == 'People' : tmp = gbwiki.getPeople(filters)
    elif gbType == 'Platforms' : tmp = gbwiki.getPlatforms(filters)
    elif gbType == 'Promos' : tmp = gbwiki.getPromos(filters)
    elif gbType == 'RatingBoards' : tmp = gbwiki.getRatingBoards(filters)
    elif gbType == 'Regions' : tmp = gbwiki.getRegions(filters)
    elif gbType == 'Releases' : tmp = gbwiki.getReleases(filters)
    elif gbType == 'Reviews' : tmp = gbwiki.getReviews(filters)
    elif gbType == 'Themes' : tmp = gbwiki.getThemes(filters)
    elif gbType == 'UserReviews' : tmp = gbwiki.getUserReviews(filters)
    else :
        print("gbType not recognized")
        return   
# Checking to see if the API call returned nothing or had an error; most of the keys
# in this test should work, but Promos do not run all the time.  This test is 
# mainly to prevent a lack of promos from breaking the test
    if tmp == None : return
# Prints off the attributes common to all objects except those that do not
# inherit from GBObject
    if gbType == 'GameRatings' : 
        for item in tmp :
            print(item.api_detail_url)
            print(item.guid)
            print(item.id)
            print(item.image_urls)
            print(item.name)
            print(item.rating_board)
    elif gbType == 'Regions' :
        for item in tmp :
            print(item.api_detail_url)
            print(item.date_added)
            print(item.date_last_updated)
            print(item.deck)
            print(item.description)
            print(item.guid)
            print(item.id)
            print(item.image_urls)
            print(item.name)
    elif gbType == 'Reviews' :
        for item in tmp :
            print(item.api_detail_url)
            print(item.deck)
            print(item.description)
            print(item.dlc_name)
            print(item.game)
            print(item.guid)
            print(item.id)
            print(item.platforms)
            print(item.publish_date)
            print(item.release)
            print(item.reviewer)
            print(item.score)
            print(item.site_detail_url)
    elif gbType == 'Themes' :
        for item in tmp :
            print(item.api_detail_url)
            print(item.guid)
            print(item.id)
            print(item.name)
            print(item.site_detail_url)
    elif gbType == 'UserReviews' :
        for item in tmp :
            print(item.api_detail_url)
            print(item.date_added)
            print(item.date_last_updated)
            print(item.deck)
            print(item.description)
            print(item.game)
            print(item.release)
            print(item.dlc)
            print(item.guid)
            print(item.id)
            print(item.reviewer)
            print(item.score)
            print(item.site_detail_url)
    elif gbType in ['Accessories', 'Characters', 'Companies', 'Concepts', 'DLCs', 'Franchises', 'Games', 'Genres', 'Locations', 'Objects', 'People', 'Platforms', 'Promos', 'RatingBoards', 'Releases'] :
        for item in tmp :
            print(item.api_detail_url)
            print(item.date_added)
            print(item.date_last_updated)
            print(item.deck)
            print(item.description)
            print(item.guid)
            print(item.id)
            print(item.image_urls)
            print(item.name)
            print(item.site_detail_url) 
    else :
        print("gbType not recognized")
        return  
    print("\n")
    return

manual_run = input("Preparing to run unit tests for gbwiki.py.  Do you want each test to run only after you press the enter key (y/n)?")
#Initializing the common filters dictionary which will be used for the MultipleTests
filters = dict()

#Unit test for getAccessory() function
print("TESTING GETACCESSORY()")
runSingleTest('Accessory', '3000-111')
autoChk()

#Unit test for getAccessories() function
print("TESTING GETACCESSORIES()")
filters["name"] = "mouse"
runMultipleTest('Accessories', filters)
autoChk()

#Unit test for getCharacter() function
print("TESTING GETCHARACTER()")
runSingleTest('Character', '3005-25044')
autoChk()

#Unit test for getCharacters() function
print("TESTING GETCHARACTERS()")
filters["name"] = "Jill"
runMultipleTest('Characters', filters)
autoChk()

#Unit test for getCompany() function
print("TESTING GETCOMPANY()")
runSingleTest('Company', '3010-7025')
autoChk()


#Unit test for getCharacters() function
print("TESTING GETCOMPANIES()")
filters["name"] = "Nintendo"
runMultipleTest('Companies', filters)
autoChk()


#Unit test for getConcept() function
print("TESTING GETCONCEPT()")
runSingleTest('Concept', '3015-9701')
autoChk()


#Unit test for getCharacters() function
print("TESTING GETCONCEPTS()")
filters["name"] = "Kamaitachi"
runMultipleTest('Concepts', filters)
autoChk()


#Unit test for getDLC() function
print("TESTING GETDLC()")
runSingleTest('DLC', '3020-1010')
autoChk()


#Unit test for getDLCs() function
print("TESTING GETDLCs()")
filters["name"] = "The Pitt"
runMultipleTest('DLCs', filters)
autoChk()


#Unit test for getFranchise() function
print("TESTING GETFRANCHISE()")
runSingleTest('Franchise', '3025-4933')
autoChk()


#Unit test for getFranchises() function
print("TESTING GETFRANCHISES()")
filters["name"] = "Street Fighter"
runMultipleTest('Franchises', filters)
autoChk()


#Unit test for getGame() function
print("TESTING GETGAME()")
runSingleTest('Game', '3030-12300')
autoChk()

#Unit test for getGames() function
print("TESTING GETGAMES()")
filters["name"] = "Tetris"
runMultipleTest('Games', filters)
autoChk()


#Unit test for getGameRating() function
print("TESTING GETGAMERATING()")
runSingleTest('GameRating', '3065-34')
autoChk()

#Unit test for getGameRatings() function
print("TESTING GETGAMERATINGS()")
filters["name"] = "ESRB"
runMultipleTest('GameRatings', filters)
autoChk()


#Unit test for getGenre() function
print("TESTING GETGENRE()")
runSingleTest('Genre', '3060-16')
autoChk()

#Unit test for getGenres() function
print("TESTING GETGENRES()")
filters["name"] = "role-playing"
runMultipleTest('Genres', filters)
autoChk()


#Unit test for getLocation() function
print("TESTING GETLOCATION()")
runSingleTest('Location', '3035-5610')
autoChk()

#Unit test for getLocations() function
print("TESTING GETLOCATIONS()")
filters["name"] = "Texas"
runMultipleTest('Locations', filters)
autoChk()


#Unit test for getObject() function
print("TESTING GETOBJECT()")
runSingleTest('Object', '3055-1')
autoChk()

#Unit test for getObjects() function
print("TESTING GETOBJECTS()")
filters["name"] = "fireball"
runMultipleTest('Objects', filters)
autoChk()


#Unit test for getPerson() function
print("TESTING GETPERSON()")
runSingleTest('Person', '3040-46955')
autoChk()

#Unit test for getPeople() function
print("TESTING GETPEOPLE()")
filters["name"] = "Sega"
runMultipleTest('People', filters)
autoChk()


#Unit test for getPlatform() function
print("TESTING GETPLATFORM()")
runSingleTest('Platform', '3045-178')
autoChk()

#Unit test for getPlatforms() function
print("TESTING GETPLATFORMS()")
filters["name"] = "Dreamcast"
runMultipleTest('Platforms', filters)
autoChk()


#Unit test for getPromo() function
#As of 9/14/20, there are no promos in the system
print("TESTING GETPROMO()")
runSingleTest('Promo', '3045-178')
autoChk()

#Unit test for getPromos() function
#As of 9/14/20, there are no promos in the system
print("TESTING GETPROMOS()")
filters = dict()
runMultipleTest('Promos', filters)
autoChk()


#Unit test for getRatingBoard() function
print("TESTING GETRATINGBOARD()")
runSingleTest('RatingBoard', '3070-1')
autoChk()

#Unit test for getRatingBoards() function
print("TESTING GETRATINGBOARDS()")
filters["name"] = "PEGI"
runMultipleTest('RatingBoards', filters)
autoChk()


#Unit test for getRegion() function
print("TESTING GETREGION()")
runSingleTest('Region','3075-1')
autoChk()

#Unit test for getRegions() function
print("TESTING GETREGIONS()")
filters["name"] = "Australia"
runMultipleTest('Regions', filters)
autoChk()


#Unit test for getRelease() function
print("TESTING GETRELEASE()")
runSingleTest('Release', '3050-995')
autoChk()

#Unit test for getReleases() function
print("TESTING GETRELEASES()")
filters["name"] = "Mario"
runMultipleTest('Releases', filters)
autoChk()


#Unit test for getReview() function
print("TESTING GETREVIEW()")
runSingleTest('Review', '1900-700')
autoChk()

#Unit test for getReviews() function
print("TESTING GETREVIEWS()")
filters["game"] = "Saints row"
runMultipleTest('Reviews', filters)
autoChk()



#Unit test for search() function
print("TESTING SEARCH()")
results = gbwiki.search("Luchadeer")
for item in results :
    print(item.api_detail_url)
    print(item.date_added)
    print(item.date_last_updated)
    print(item.deck)
    print(item.description)
    print(item.guid)
    print(item.id)
    print(item.image_urls)
    print(item.name)
    print(item.site_detail_url)
    print(item.resource_type)
    print("\n")

autoChk()


#Unit test for getTheme() function
print("TESTING GETTHEME()")
runSingleTest('Theme', '3032-19')
autoChk()

#Unit test for getThemes() function
print("TESTING GETTHEMES()")
filters["name"] = "western"
runMultipleTest('Themes', filters)
autoChk()


#Unit test for getTypes() function
print("TESTING GETTYPES()")
filters = dict()
accresults = gbwiki.getTypes()
for item in accresults :
    print(item.detail_resource_name)
    print(item.id)
    print(item.list_resource_name)
    print("\n")

autoChk()


#Unit test for getUserReview() function
print("TESTING GETUSERREVIEW()")
runSingleTest('UserReview', '2200-52')
autoChk()

#Unit test for getUserReviews() function
print("TESTING GETUSERREVIEWS()")
filters["game"] = "Halo"
runMultipleTest('UserReviews', filters)
autoChk()

