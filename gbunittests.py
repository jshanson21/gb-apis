import gbclass

#Unit test for getAccessory() function
print("TESTING GETACCESSORY()")
tmpacc = gbclass.getAccessory('3000-111')
print(tmpacc["results"]["name"])
print(tmpacc["results"]["description"])
print("\n")

tmp = input("Press Enter to continue")


#Unit test for getAccessories() function
print("TESTING GETACCESSORIES()")
filters = dict()
filters["name"] = "Ring-Con"
filters["date_added"] = "2019-12-15 19:45:28"
accresults = gbclass.getAccessories(filters)
tmpaccs = accresults["results"]
for item in tmpaccs :
    print(item["name"])
    print(item["description"])
    print(item["guid"])
    print("\n")


tmp = input("Press Enter to continue")

#Unit test for getCharacter() function
print("TESTING GETCHARACTER()")
tmpacc = gbclass.getCharacter('3005-25044')
print(tmpacc["results"]["name"])
print(tmpacc["results"]["description"])
print("\n")

tmp = input("Press Enter to continue")


#Unit test for getCharacters() function
print("TESTING GETCHARACTERS()")
filters = dict()
filters["name"] = "Jill"
#filters["date_added"] = "2019-12-15 19:45:28"
accresults = gbclass.getCharacters(filters)
tmpaccs = accresults["results"]
for item in tmpaccs :
    print(item["name"])
    print(item["description"])
    print(item["guid"])
    print("\n")

tmp = input("Press Enter to continue")


#Unit test for getChat() function
print("TESTING GETCHAT()")
tmpacc = gbclass.getChat('2450-981')
print(tmpacc["results"]["channel_name"])
print(tmpacc["results"]["deck"])
print("\n")

tmp = input("Press Enter to continue")


#Unit test for getChats() function
print("TESTING GETCHATS()")
filters = dict()
#filters["name"] = "Jill"
#filters["date_added"] = "2019-12-15 19:45:28"
accresults = gbclass.getChats(filters)
tmpaccs = accresults["results"]
for item in tmpaccs :
    print(item["channel_name"])
    print(item["deck"])
    print(item["guid"])
    print("\n")

tmp = input("Press Enter to continue")

#Unit test for getCompany() function
print("TESTING GETCOMPANY()")
tmpacc = gbclass.getCompany('3010-386')
print(tmpacc["results"]["name"])
print(tmpacc["results"]["description"])
print("\n")

tmp = input("Press Enter to continue")


#Unit test for getCharacters() function
print("TESTING GETCOMPANIES()")
filters = dict()
filters["name"] = "Nintendo"
#filters["date_added"] = "2019-12-15 19:45:28"
accresults = gbclass.getCompanies(filters)
tmpaccs = accresults["results"]
for item in tmpaccs :
    print(item["name"])
    print(item["description"])
    print(item["guid"])
    print("\n")

tmp = input("Press Enter to continue")


#Unit test for getConcept() function
print("TESTING GETCONCEPT()")
tmpacc = gbclass.getConcept('3015-9701')
print(tmpacc["results"]["name"])
print(tmpacc["results"]["description"])
print("\n")

tmp = input("Press Enter to continue")


#Unit test for getCharacters() function
print("TESTING GETCONCEPTS()")
filters = dict()
filters["name"] = "Kamaitachi"
#filters["date_added"] = "2019-12-15 19:45:28"
accresults = gbclass.getConcepts(filters)
tmpaccs = accresults["results"]
for item in tmpaccs :
    print(item["name"])
    print(item["description"])
    print(item["guid"])
    print("\n")

tmp = input("Press Enter to continue")


#Unit test for getDLC() function
print("TESTING GETDLC()")
tmpacc = gbclass.getDLC('3020-1010')
print(tmpacc["results"]["name"])
print(tmpacc["results"]["description"])
print("\n")

tmp = input("Press Enter to continue")


#Unit test for getDLCs() function
print("TESTING GETDLCs()")
filters = dict()
filters["name"] = "The Pitt"
#filters["date_added"] = "2019-12-15 19:45:28"
accresults = gbclass.getDLCs(filters)
tmpaccs = accresults["results"]
for item in tmpaccs :
    print(item["name"])
    print(item["description"])
    print(item["guid"])
    print("\n")

tmp = input("Press Enter to continue")


#Unit test for getFranchise() function
print("TESTING GETFRANCHISE()")
tmpacc = gbclass.getFranchise('3025-4933')
print(tmpacc["results"]["name"])
print(tmpacc["results"]["description"])
print("\n")

tmp = input("Press Enter to continue")


#Unit test for getFranchises() function
print("TESTING GETFRANCHISES()")
filters = dict()
filters["name"] = "Street Fighter"
#filters["date_added"] = "2019-12-15 19:45:28"
accresults = gbclass.getFranchises(filters)
tmpaccs = accresults["results"]
for item in tmpaccs :
    print(item["name"])
    print(item["description"])
    print(item["guid"])
    print("\n")

tmp = input("Press Enter to continue")


#Unit test for getGame() function
print("TESTING GETGAME()")
tmpgame = gbclass.getGame('3030-12300')
print(tmpgame["results"]["name"])
print(tmpgame["results"]["description"])
print("\n")


tmp = input("Press Enter to continue")

#Unit test for getGames() function
print("TESTING GETGAMES()")
filters = dict()
filters["name"] = "Tetris"
#filters["date_added"] = "2019-12-15 19:45:28"
accresults = gbclass.getGames(filters)
tmpaccs = accresults["results"]
for item in tmpaccs :
    print(item["name"])
    print(item["description"])
    print(item["guid"])
    print("\n")

tmp = input("Press Enter to continue")


#Unit test for getGameRating() function
print("TESTING GETGAMERATING()")
tmpgame = gbclass.getGameRating('3065-34')
print(tmpgame["results"]["name"])
print(tmpgame["results"]["rating_board"]["name"])
print("\n")


tmp = input("Press Enter to continue")

#Unit test for getGameRatings() function
print("TESTING GETGAMERATINGS()")
filters = dict()
filters["name"] = "ESRB"
#filters["date_added"] = "2019-12-15 19:45:28"
accresults = gbclass.getGameRatings(filters)
tmpaccs = accresults["results"]
for item in tmpaccs :
    print(item["name"])
    print(item["rating_board"]["name"])
    print(item["guid"])
    print("\n")

tmp = input("Press Enter to continue")


#Unit test for getGenre() function
print("TESTING GETGENRE()")
tmpgame = gbclass.getGenre('3060-16')
print(tmpgame["results"]["name"])
print(tmpgame["results"]["description"])
print("\n")


tmp = input("Press Enter to continue")

#Unit test for getGenres() function
print("TESTING GETGENRES()")
filters = dict()
filters["name"] = "role-playing"
#filters["date_added"] = "2019-12-15 19:45:28"
accresults = gbclass.getGenres(filters)
tmpaccs = accresults["results"]
for item in tmpaccs :
    print(item["name"])
    print(item["description"])
    print(item["guid"])
    print("\n")

tmp = input("Press Enter to continue")


#Unit test for getImage() function
#Commented out for now
#print("TESTING GETIMAGE()")
#tmpgame = gbclass.getImage('1300-2279986')
#print(tmpgame["results"]["original_url"])
#print(tmpgame["results"]["image_tag"])
#print("\n")


#Unit test for getLocation() function
print("TESTING GETLOCATION()")
tmpgame = gbclass.getLocation('3035-5610')
print(tmpgame["results"]["name"])
print(tmpgame["results"]["description"])
print("\n")


tmp = input("Press Enter to continue")

#Unit test for getLocations() function
print("TESTING GETLOCATIONS()")
filters = dict()
filters["name"] = "Texas"
#filters["date_added"] = "2019-12-15 19:45:28"
accresults = gbclass.getLocations(filters)
tmpaccs = accresults["results"]
for item in tmpaccs :
    print(item["name"])
    print(item["description"])
    print(item["guid"])
    print("\n")

tmp = input("Press Enter to continue")


#Unit test for getObject() function
print("TESTING GETOBJECT()")
tmpgame = gbclass.getObject('3055-1')
print(tmpgame["results"]["name"])
print(tmpgame["results"]["description"])
print("\n")


tmp = input("Press Enter to continue")

#Unit test for getObjects() function
print("TESTING GETOBJECTS()")
filters = dict()
filters["name"] = "fireball"
#filters["date_added"] = "2019-12-15 19:45:28"
accresults = gbclass.getObjects(filters)
tmpaccs = accresults["results"]
for item in tmpaccs :
    print(item["name"])
    print(item["description"])
    print(item["guid"])
    print("\n")

tmp = input("Press Enter to continue")


#Unit test for getPerson() function
print("TESTING GETPERSON()")
tmpgame = gbclass.getPerson('3040-46955')
print(tmpgame["results"]["name"])
print(tmpgame["results"]["description"])
print("\n")


tmp = input("Press Enter to continue")

#Unit test for getPeople() function
print("TESTING GETPEOPLE()")
filters = dict()
filters["name"] = "Sega"
#filters["date_added"] = "2019-12-15 19:45:28"
accresults = gbclass.getPeople(filters)
tmpaccs = accresults["results"]
for item in tmpaccs :
    print(item["name"])
    print(item["description"])
    print(item["guid"])
    print("\n")

tmp = input("Press Enter to continue")


#Unit test for getPlatform() function
print("TESTING GETPLATFORM()")
tmpgame = gbclass.getPlatform('3045-178')
print(tmpgame["results"]["name"])
print(tmpgame["results"]["description"])
print("\n")


tmp = input("Press Enter to continue")

#Unit test for getPlatforms() function
print("TESTING GETPLATFORMS()")
filters = dict()
filters["name"] = "Dreamcast"
#filters["date_added"] = "2019-12-15 19:45:28"
accresults = gbclass.getPlatforms(filters)
tmpaccs = accresults["results"]
for item in tmpaccs :
    print(item["name"])
    print(item["description"])
    print(item["guid"])
    print("\n")

tmp = input("Press Enter to continue")


#Unit test for getPromo() function
#As of 9/14/20, there are no promos in the system
print("TESTING GETPROMO()")
tmpgame = gbclass.getPromo('3045-178')
if tmpgame["results"] != [] :
    print(tmpgame["results"]["name"])
    print(tmpgame["results"]["description"])
print("\n")


tmp = input("Press Enter to continue")

#Unit test for getPromos() function
#As of 9/14/20, there are no promos in the system
print("TESTING GETPROMOS()")
filters = dict()
#filters["name"] = "Dreamcast"
#filters["date_added"] = "2019-12-15 19:45:28"
accresults = gbclass.getPromos(filters)
tmpaccs = accresults["results"]
if tmpaccs != [] :
    for item in tmpaccs :
        print(item["name"])
        print(item["description"])
        print(item["guid"])
print("\n")

tmp = input("Press Enter to continue")


#Unit test for getRatingBoard() function
print("TESTING GETRATINGBOARD()")
tmpgame = gbclass.getRatingBoard('3070-1')
print(tmpgame["results"]["name"])
print(tmpgame["results"]["description"])
print("\n")


tmp = input("Press Enter to continue")

#Unit test for getRatingBoards() function
print("TESTING GETRATINGBOARDS()")
filters = dict()
filters["name"] = "PEGI"
#filters["date_added"] = "2019-12-15 19:45:28"
accresults = gbclass.getRatingBoards(filters)
tmpaccs = accresults["results"]
for item in tmpaccs :
    print(item["name"])
    print(item["description"])
    print(item["guid"])
    print("\n")

tmp = input("Press Enter to continue")


#Unit test for getRegion() function
print("TESTING GETREGION()")
tmpgame = gbclass.getRegion('3075-1')
print(tmpgame["results"]["name"])
print(tmpgame["results"]["description"])
print("\n")


tmp = input("Press Enter to continue")

#Unit test for getRegions() function
print("TESTING GETREGIONS()")
filters = dict()
filters["name"] = "Australia"
#filters["date_added"] = "2019-12-15 19:45:28"
accresults = gbclass.getRegions(filters)
tmpaccs = accresults["results"]
for item in tmpaccs :
    print(item["name"])
    print(item["description"])
    print(item["guid"])
    print("\n")

tmp = input("Press Enter to continue")


#Unit test for getRelease() function
print("TESTING GETRELEASE()")
tmpgame = gbclass.getRelease('3050-995')
print(tmpgame["results"]["name"])
print(tmpgame["results"]["description"])
print("\n")


tmp = input("Press Enter to continue")

#Unit test for getReleases() function
print("TESTING GETRELEASES()")
filters = dict()
filters["name"] = "Mario"
#filters["date_added"] = "2019-12-15 19:45:28"
accresults = gbclass.getReleases(filters)
tmpaccs = accresults["results"]
for item in tmpaccs :
    print(item["name"])
    print(item["description"])
    print(item["guid"])
    print("\n")

tmp = input("Press Enter to continue")



#Unit test for getReview() function
print("TESTING GETREVIEW()")
tmpgame = gbclass.getReview('1900-700')
print(tmpgame["results"]["game"]["name"])
print(tmpgame["results"]["deck"])
print("\n")


tmp = input("Press Enter to continue")

#Unit test for getReviews() function
print("TESTING GETREVIEWS()")
filters = dict()
filters["game"] = "Saints row"
#filters["date_added"] = "2019-12-15 19:45:28"
accresults = gbclass.getReviews(filters)
tmpaccs = accresults["results"]
for item in tmpaccs :
    print(item["game"]["name"])
    print(item["deck"])
    print(item["guid"])
    print("\n")

tmp = input("Press Enter to continue")



#Unit test for search() function
print("TESTING SEARCH()")
results = gbclass.search("Luchadeer")
entries = results["results"]
for item in entries :
    print(item["name"])
    print(item["site_detail_url"])
    print(item["guid"])
    print(item["resource_type"])
    print("\n")


tmp = input("Press Enter to continue")


#Unit test for getTheme() function
print("TESTING GETTHEME()")
tmpgame = gbclass.getTheme('3032-19')
print(tmpgame["results"]["name"])
print(tmpgame["results"]["guid"])
print("\n")


tmp = input("Press Enter to continue")

#Unit test for getThemes() function
print("TESTING GETTHEMES()")
filters = dict()
filters["name"] = "western"
#filters["date_added"] = "2019-12-15 19:45:28"
accresults = gbclass.getThemes(filters)
tmpaccs = accresults["results"]
for item in tmpaccs :
    print(item["name"])
    print(item["guid"])
    print("\n")

tmp = input("Press Enter to continue")


#Unit test for getTypes() function
print("TESTING GETTYPES()")
filters = dict()
#filters["name"] = "western"
#filters["date_added"] = "2019-12-15 19:45:28"
accresults = gbclass.getTypes(filters)
tmpaccs = accresults["results"]
for item in tmpaccs :
    print(item["list_resource_name"])
    print(item["id"])
    print("\n")

tmp = input("Press Enter to continue")


#Unit test for getUserReview() function
print("TESTING GETUSERREVIEW()")
tmpgame = gbclass.getUserReview('2200-52')
print(tmpgame["results"]["game"]["name"])
print(tmpgame["results"]["score"])
print("\n")


tmp = input("Press Enter to continue")

#Unit test for getUserReviews() function
print("TESTING GETUSERREVIEWS()")
filters = dict()
filters["game"] = "Halo"
#filters["date_added"] = "2019-12-15 19:45:28"
accresults = gbclass.getUserReviews(filters)
tmpaccs = accresults["results"]
for item in tmpaccs :
    if item["game"] is not None :
        print(item["game"]["name"])
    print(item["score"])
    print(item["guid"])
    print("\n")

tmp = input("Press Enter to continue")


#Unit test for getVideo() function
print("TESTING GETVIDEO()")
tmpgame = gbclass.getVideo('2970-12353')
print(tmpgame["results"]["name"])
print(tmpgame["results"]["deck"])
print("\n")


tmp = input("Press Enter to continue")

#Unit test for getVideos() function
print("TESTING GETVIDEOS()")
filters = dict()
filters["name"] = "breaking brad"
#filters["date_added"] = "2019-12-15 19:45:28"
accresults = gbclass.getVideos(filters)
tmpaccs = accresults["results"]
for item in tmpaccs :
    print(item["name"])
    print(item["deck"])
    print(item["guid"])
    print("\n")

tmp = input("Press Enter to continue")


#Unit test for getVideoCategory() function
print("TESTING GETVIDEOCATEGORY()")
tmpgame = gbclass.getVideoCategory('3')
print(tmpgame["results"]["name"])
print(tmpgame["results"]["deck"])
print("\n")


tmp = input("Press Enter to continue")

#Unit test for getVideoCategories() function
print("TESTING GETVIDEOCATEGORIES()")
filters = dict()
filters["name"] = "old games"
#filters["date_added"] = "2019-12-15 19:45:28"
accresults = gbclass.getVideoCategories(filters)
tmpaccs = accresults["results"]
for item in tmpaccs :
    print(item["name"])
    print(item["deck"])
    print(item["id"])
    print("\n")

tmp = input("Press Enter to continue")


#Unit test for getVideoShow() function
print("TESTING GETVIDEOSHOW()")
tmpgame = gbclass.getVideoShow('2340-93')
print(tmpgame["results"]["title"])
print(tmpgame["results"]["deck"])
print("\n")


tmp = input("Press Enter to continue")

#Unit test for getVideoCategories() function
print("TESTING GETVIDEOSHOWS()")
filters = dict()
filters["name"] = "mario madness"
#filters["date_added"] = "2019-12-15 19:45:28"
accresults = gbclass.getVideoShows(filters)
tmpaccs = accresults["results"]
for item in tmpaccs :
    print(item["title"])
    print(item["deck"])
    print(item["id"])
    print("\n")

tmp = input("Press Enter to continue")


#Unit test for getCurrentLive() function
print("TESTING GETCURRENTLIVE()")
tmpgame = gbclass.getCurrentLive()
if tmpgame["video"] != None :
    print(tmpgame["results"]["name"])
    print(tmpgame["results"]["deck"])
print("\n")


tmp = input("Press Enter to continue")


#Unit test for getAllSavedTimes() function
print("TESTING GETALLSAVEDTIMES()")
accresults = gbclass.getAllSavedTimes()
tmpaccs = accresults["savedTimes"]
vid_id = None
for item in tmpaccs :
    print(item["videoId"])
    print(item["savedTime"])
    print(item["savedOn"])
    vid_id = item["videoId"]
    print("\n")

tmp = input("Press Enter to continue")



#Unit test for getSavedTime() function; it takes in the last video_id from the previous
#function
print("TESTING GETSAVEDTIME()")
#filters["date_added"] = "2019-12-15 19:45:28"
accresults = gbclass.getSavedTime(vid_id)
print(accresults['savedTime'])


tmp = input("Press Enter to continue")


#Unit test for saveTime() function; it takes in the last video_id from the previous
#function
print("TESTING SAVETIME()")
time = '2'
accresults = gbclass.saveTime(vid_id, time)


tmp = input("Press Enter to continue")
