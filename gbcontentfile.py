# Returns the appropriate base URL based on the type of GB Object that would be needed
# If the gbType is invalid, "None" is returned
def getSingleBaseUrl(gbType) :
    if gbType == 'Accessory' : return 'https://www.giantbomb.com/api/accessory/'
    elif gbType == 'Character' : return 'https://www.giantbomb.com/api/character/'
    elif gbType == 'Company' : return 'https://www.giantbomb.com/api/company/'
    elif gbType == 'Concept' : return 'https://www.giantbomb.com/api/concept/'
    elif gbType == 'DLC' : return 'https://www.giantbomb.com/api/dlc/'
    elif gbType == 'Franchise' : return 'https://www.giantbomb.com/api/franchise/'
    elif gbType == 'Game' : return 'https://www.giantbomb.com/api/game/'
    elif gbType == 'GameRating' : return 'https://www.giantbomb.com/api/game_rating/'
    elif gbType == 'Genre' : return 'https://www.giantbomb.com/api/genre/'
    elif gbType == 'Location' : return 'https://www.giantbomb.com/api/location/'
    elif gbType == 'Object' : return 'https://www.giantbomb.com/api/object/'
    elif gbType == 'Person' : return 'https://www.giantbomb.com/api/person/'
    elif gbType == 'Platform' : return 'https://www.giantbomb.com/api/platform/'
    elif gbType == 'Promo' : return 'https://www.giantbomb.com/api/promo/'
    elif gbType == 'RatingBoard' : return 'https://www.giantbomb.com/api/rating_board/'
    elif gbType == 'Region' : return 'https://www.giantbomb.com/api/region/'
    elif gbType == 'Release' : return 'https://www.giantbomb.com/api/release/'
    elif gbType == 'Review' : return 'https://www.giantbomb.com/api/review/'
    elif gbType == 'Theme' : return 'https://www.giantbomb.com/api/theme/'
    elif gbType == 'UserReview' : return 'https://www.giantbomb.com/api/user_review/'
    elif gbType == 'Video' : return 'https://www.giantbomb.com/api/video/'
    elif gbType == 'VideoCategory' : return 'https://www.giantbomb.com/api/video_category/'
    elif gbType == 'VideoShow' : return 'https://www.giantbomb.com/api/video_show/'
    else :
        print("gbType not recognized")
        return None


# Returns the appropriate error message to use based on the gbType.
# If the gbType is invalid, then "None" is returned
def getSingleErrorMessage(gbType) :
    if gbType == 'Accessory' : return '===Could Not Retrieve Accessory==='
    elif gbType == 'Character' : return '===Could Not Retrieve Character==='
    elif gbType == 'Company' : return '===Could Not Retrieve Company==='
    elif gbType == 'Concept' : return '===Could Not Retrieve Concept==='
    elif gbType == 'DLC' : return '===Could Not Retrieve DLC==='
    elif gbType == 'Franchise' : return '===Could Not Retrieve Franchise==='
    elif gbType == 'Game' : return '===Could Not Retrieve Game==='
    elif gbType == 'GameRating' : return '===Could Not Retrieve Game Rating==='
    elif gbType == 'Genre' : return '===Could Not Retrieve Genre==='
    elif gbType == 'Location' : return '===Could Not Retrieve Location==='
    elif gbType == 'Object' : return '===Could Not Retrieve Object==='
    elif gbType == 'Person' : return '===Could Not Retrieve Person==='
    elif gbType == 'Platform' : return '===Could Not Retrieve Platform==='
    elif gbType == 'Promo' : return '===Could Not Retrieve Promo==='
    elif gbType == 'RatingBoard' : return '===Could Not Retrieve Rating Board==='
    elif gbType == 'Region' : return '===Could Not Retrieve Region==='
    elif gbType == 'Release' : return '===Could Not Retrieve Release==='
    elif gbType == 'Review' : return '===Could Not Retrieve Review==='
    elif gbType == 'Theme' : return '===Could Not Retrieve Theme==='
    elif gbType == 'UserReview' : return '===Could Not Retrieve User Review==='
    elif gbType == 'Video' : return '===Could Not Retrieve Video==='
    elif gbType == 'VideoCategory' : return '===Could Not Retrieve Video Category==='
    elif gbType == 'VideoShow' : return '===Could Not Retrieve Video Show==='
    else :
        print("gbType not recognized")
        return None




# Returns the appropriate base URL based on the type of GB Object that would be needed
# If the gbType is invalid, "None" is returned
def getMultipleBaseUrl(gbType) :
    if gbType == 'Accessories' : return 'https://www.giantbomb.com/api/accessories/?'
    elif gbType == 'Characters' : return 'https://www.giantbomb.com/api/characters/?'
    elif gbType == 'Companies' : return 'https://www.giantbomb.com/api/companies/?'
    elif gbType == 'Concepts' : return 'https://www.giantbomb.com/api/concepts/?'
    elif gbType == 'DLCs' : return 'https://www.giantbomb.com/api/dlcs/?'
    elif gbType == 'Franchises' : return 'https://www.giantbomb.com/api/franchises/?'
    elif gbType == 'Games' : return 'https://www.giantbomb.com/api/games/?'
    elif gbType == 'GameRatings' : return 'https://www.giantbomb.com/api/game_ratings/?'
    elif gbType == 'Genres' : return 'https://www.giantbomb.com/api/genres/?'
    elif gbType == 'Locations' : return 'https://www.giantbomb.com/api/locations/?'
    elif gbType == 'Objects' : return 'https://www.giantbomb.com/api/objects/?'
    elif gbType == 'People' : return 'https://www.giantbomb.com/api/people/?'
    elif gbType == 'Platforms' : return 'https://www.giantbomb.com/api/platforms/?'
    elif gbType == 'Promos' : return 'https://www.giantbomb.com/api/promos/?'
    elif gbType == 'RatingBoards' : return 'https://www.giantbomb.com/api/rating_boards/?'
    elif gbType == 'Regions' : return 'https://www.giantbomb.com/api/regions/?'
    elif gbType == 'Releases' : return 'https://www.giantbomb.com/api/releases/?'
    elif gbType == 'Reviews' : return 'https://www.giantbomb.com/api/reviews/?'
    elif gbType == 'Search' : return 'https://www.giantbomb.com/api/search/?'
    elif gbType == 'Themes' : return 'https://www.giantbomb.com/api/themes/?'
    elif gbType == 'UserReviews' : return 'https://www.giantbomb.com/api/user_reviews/?'
    elif gbType == 'Videos' : return 'https://www.giantbomb.com/api/videos/?'
    elif gbType == 'VideoCategories' : return 'https://www.giantbomb.com/api/video_categories/?'
    elif gbType == 'VideoShows' : return 'https://www.giantbomb.com/api/video_shows/?'
    else :
        print("gbType not recognized")
        return None


# Returns the appropriate error message to use based on the gbType.
# If the gbType is invalid, then "None" is returned
def getMultipleErrorMessage(gbType) :
    if gbType == 'Accessories' : return '===Could Not Retrieve Any Accessories==='
    elif gbType == 'Characters' : return '===Could Not Retrieve Any Characters==='
    elif gbType == 'Companies' : return '===Could Not Retrieve Any Companies==='
    elif gbType == 'Concepts' : return '===Could Not Retrieve Any Concepts==='
    elif gbType == 'DLCs' : return '===Could Not Retrieve Any DLCs==='
    elif gbType == 'Franchises' : return '===Could Not Retrieve Any Franchises==='
    elif gbType == 'Games' : return '===Could Not Retrieve Any Games==='
    elif gbType == 'GameRatings' : return '===Could Not Retrieve Any Game Ratings==='
    elif gbType == 'Genres' : return '===Could Not Retrieve Any Genres==='
    elif gbType == 'Locations' : return '===Could Not Retrieve Any Locations==='
    elif gbType == 'Objects' : return '===Could Not Retrieve Any Objects==='
    elif gbType == 'People' : return '===Could Not Retrieve Any People==='
    elif gbType == 'Platforms' : return '===Could Not Retrieve Any Platforms==='
    elif gbType == 'Promos' : return '===Could Not Retrieve Any Promos==='
    elif gbType == 'RatingBoards' : return '===Could Not Retrieve Any Rating Boards==='
    elif gbType == 'Regions' : return '===Could Not Retrieve Any Regions==='
    elif gbType == 'Releases' : return '===Could Not Retrieve Any Releases==='
    elif gbType == 'Reviews' : return '===Could Not Retrieve Any Reviews==='
    elif gbType == 'Search' : return '===Search error or no results found==='
    elif gbType == 'Themes' : return '===Could Not Retrieve Any Themes==='
    elif gbType == 'UserReviews' : return '===Could Not Retrieve Any User Reviews==='
    elif gbType == 'Videos' : return '===Could Not Retrieve Any Videos==='
    elif gbType == 'VideoCategories' : return '===Could Not Retrieve Any Video Categories==='
    elif gbType == 'VideoShows' : return '===Could Not Retrieve Any Video Shows==='
    else :
        print("gbType not recognized")
        return None


