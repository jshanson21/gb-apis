import json

class GBObject:

    def __init__(self, jsdata):
        self.api_detail_url = jsdata['api_detail_url']
        self.date_added = jsdata['date_added']
        self.date_last_updated = jsdata['date_last_updated']
        self.deck = jsdata['deck']
        self.description = jsdata['description']
        self.guid = jsdata['guid']
        self.id = jsdata['id']
        self.image_urls = jsdata['image']
        self.name = jsdata['name']
        self.site_detail_url = jsdata['site_detail_url']


class Accessory(GBObject):

    def __init__(self, jsdata):
        super().__init__(jsdata)

        self.image_tags = jsdata['image_tags']


class Character(GBObject):

    def __init__(self, jsdata):
        super().__init__(jsdata)
    # Consider creating some kind of object to use for concepts,
    #enemies, first_appeared_in_game, franchises, friends, games, locations
    #objects, and people.  For now, they're just lists of dictionaries
        self.aliases = jsdata['aliases']
        self.birthday = jsdata['birthday']
        self.concepts = jsdata['concepts']
        self.enemies = jsdata['enemies']
        self.first_appeared_in_game = jsdata['first_appeared_in_game']
        self.franchises = jsdata['franchises']
        self.friends = jsdata['friends']
        self.games = jsdata['games']
        self.gender = jsdata['gender']
        self.image_tags = jsdata['image_tags']
        self.last_name = jsdata['last_name']
        self.locations = jsdata['locations']
        self.objects = jsdata['objects']
        self.people = jsdata['people']
        self.real_name = jsdata['real_name']


class Company(GBObject):

    def __init__(self, jsdata):
        super().__init__(jsdata)

        self.abbreviation = jsdata['abbreviation']
        self.aliases = jsdata['aliases']
        self.characters = jsdata['characters']
        self.concepts = jsdata['concepts']
        self.date_founded = jsdata['date_founded']
        self.developed_games = jsdata['developed_games']
        try :
            self.developer_releases = jsdata['developer_releases']
        except :
            self.developer_releases = None
        try :
            self.distributor_releases = jsdata['distributor_releases']
        except :
            self.distributor_releases = None
        self.image_tags = jsdata['image_tags']
        self.location_address = jsdata['location_address']
        self.location_city = jsdata['location_city']
        self.location_country = jsdata['location_country']
        self.location_state = jsdata['location_state']
        self.locations = jsdata['locations']
        self.objects = jsdata['objects']
        self.objects = None
        self.people = jsdata['people']
        self.phone = jsdata['phone']
        try :
            self.published_games = jsdata['published_games']
        except :
            self.published_games = None
        try :
            self.publisher_releases = jsdata['publisher_releases']
        except : 
            self.publisher_releases = None
        self.website = jsdata['website']


class Concept(GBObject):

    def __init__(self, jsdata):
        super().__init__(jsdata)

        self.aliases = jsdata['aliases']
        self.characters = jsdata['characters']
        self.concepts = jsdata['concepts']
        self.first_appeared_in_franchise = jsdata['first_appeared_in_franchise']
        self.first_appeared_in_game = jsdata['first_appeared_in_game']
        self.franchises = jsdata['franchises']
        self.games = jsdata['games']
        self.image_tags = jsdata['image_tags']
        self.locations = jsdata['locations']
        self.objects = jsdata['objects']
        self.people = jsdata['people']
        try :
            self.related_concepts = jsdata['related_concepts']
        except :
            self.related_concepts = None


class Dlc(GBObject):

    def __init__(self, jsdata):
        super().__init__(jsdata)

        self.game = jsdata['game']
        self.platform = jsdata['platform']
        self.release_date = jsdata['release_date']


class Franchise(GBObject):

    def __init__(self, jsdata):
        super().__init__(jsdata)

        self.aliases = jsdata['aliases']
        self.characters = jsdata['characters']
        self.concepts = jsdata['concepts']
        self.games = jsdata['games']
        self.image_tags = jsdata['image_tags']
        self.locations = jsdata['locations']
        self.objects = jsdata['objects']
        self.people = jsdata['people']


class Game(GBObject):

    def __init__(self, jsdata):
        super().__init__(jsdata)

        self.aliases = jsdata['aliases']
        self.characters = jsdata['characters']
        self.concepts = jsdata['concepts']
        self.developers = jsdata['developers']
        self.expected_release_day = jsdata['expected_release_day']
        self.expected_release_month = jsdata['expected_release_month']
        self.expected_release_quarter = jsdata['expected_release_quarter']
        self.expected_release_year = jsdata['expected_release_year']
        self.first_appearance_characters = jsdata['first_appearance_characters']
        self.first_appearance_concepts = jsdata['first_appearance_concepts']
        self.first_appearance_locations = jsdata['first_appearance_locations']
        self.first_appearance_objects = jsdata['first_appearance_objects']
        self.first_appearance_people = jsdata['first_appearance_people']
        self.franchises = jsdata['franchises']
        self.genres = jsdata['genres']
        self.images = jsdata['images']
        self.image_tags = jsdata['image_tags']
        self.killed_characters = jsdata['killed_characters']
        self.locations = jsdata['locations']
        self.number_of_user_reviews = jsdata['number_of_user_reviews']
        self.objects = jsdata['objects']
        self.original_game_rating = jsdata['original_game_rating']
        self.original_release_date = jsdata['original_release_date']
        self.people = jsdata['people']
        self.platforms = jsdata['platforms']
        self.publishers = jsdata['publishers']
        self.releases = jsdata['releases']
        try :
            self.dlcs = jsdata['dlcs']
        except :
            self.dlcs = None
        try :
            self.reviews = jsdata['reviews']
        except :
            self.reviews = None
        self.similar_games = jsdata['similar_games']
        self.themes = jsdata['themes']
        self.videos = jsdata['videos']


#Game Ratings do not take from the generic object because they
#contain so many fewer elements than the other objects.
class GameRating:

    def __init__(self, jsdata):
        self.api_detail_url = jsdata['api_detail_url']
        self.guid = jsdata['guid']
        self.id = jsdata['id']
        self.image_urls = jsdata['image']
        self.name = jsdata['name']
        self.rating_board = jsdata['rating_board']


class Genre(GBObject):

    def __init__(self, jsdata):
        super().__init__(jsdata)


class Location(GBObject):

    def __init__(self, jsdata):
        super().__init__(jsdata) 

        self.aliases = jsdata['aliases']
        self.first_appeared_in_game = jsdata['first_appeared_in_game']
        self.image_tags = jsdata['image_tags']


class Object(GBObject):

    def __init__(self, jsdata):
        super().__init__(jsdata) 

        self.aliases = jsdata['aliases']
        self.characters = jsdata['characters']
        try :
            self.companies = jsdata['companies']
        except :
            self.companies = None
        self.concepts = jsdata['concepts']
        self.first_appeared_in_game = jsdata['first_appeared_in_game']
        self.franchises = jsdata['franchises']
        self.games = jsdata['games']
        self.image_tags = jsdata['image_tags']
        self.locations = jsdata['locations']
        try :
           self.objects = jsdata['objects']
        except :
            self.objects = None
        self.people = jsdata['people']


class Person(GBObject):

    def __init__(self, jsdata):
        super().__init__(jsdata) 

        self.aliases = jsdata['aliases']
        self.birth_date = jsdata['birth_date']
        self.characters = jsdata['characters']
        self.concepts = jsdata['concepts']
        self.country = jsdata['country']
        self.death_date = jsdata['death_date']
        self.first_credited_game = jsdata['first_credited_game']
        self.franchises = jsdata['franchises']
        self.games = jsdata['games']
        self.gender = jsdata['gender']
        self.hometown = jsdata['hometown']
        self.image_tags = jsdata['image_tags']
        self.locations = jsdata['locations']
        try :
           self.objects = jsdata['objects']
        except :
            self.objects = None
        self.people = jsdata['people']


class Platform(GBObject):

    def __init__(self, jsdata):
        super().__init__(jsdata) 

        self.abbreviation = jsdata['abbreviation']
        self.company = jsdata['company']
        self.image_tags = jsdata['image_tags']
        self.install_base = jsdata['install_base']
        self.online_support = jsdata['online_support']
        self.original_price = jsdata['original_price']
        self.release_date = jsdata['release_date']


class Promo(GBObject):

    def __init__(self, jsdata):
        super().__init__(jsdata) 

        self.link = jsdata['link']
        self.resource_type = jsdata['resource_type']
        self.user = jsdata['user']


class RatingBoard(GBObject) :

    def __init__(self, jsdata):
        super().__init__(jsdata) 

        self.region = jsdata['region']


class Region :

    def __init__(self, jsdata):
        self.api_detail_url = jsdata['api_detail_url']
        self.date_added = jsdata['date_added']
        self.date_last_updated = jsdata['date_last_updated']
        self.deck = jsdata['deck']
        self.description = jsdata['description']
        self.guid = jsdata['guid']
        self.id = jsdata['id']
        self.image_urls = jsdata['image']
        self.name = jsdata['name']
# RatingBoards do not come back if you use the multiple version of the API call.
# As opposed to taking site_detail_url from the generic object and ruining all of
# the other objects, I opted instead to handle it like this
        try :
            self.rating_boards = jsdata['rating_boards']
        except :
            self.rating_boards = None


class Release(GBObject) :

    def __init__(self, jsdata):
        super().__init__(jsdata) 

        self.developers = jsdata['developers']
        self.expected_release_day = jsdata['expected_release_day']
        self.expected_release_month = jsdata['expected_release_month']
        self.expected_release_quarter = jsdata['expected_release_quarter']
        self.expected_release_year = jsdata['expected_release_year']
        self.game = jsdata['game']
        self.game_rating = jsdata['game_rating']
        self.maximum_players = jsdata['maximum_players']
        self.minimum_players = jsdata['minimum_players']
        try :
            self.multiplayer_features = jsdata['multiplayer_features']
        except :
            self.multiplayer_features = None
        self.platform = jsdata['platform']
        self.product_code_type = jsdata['product_code_type']
        self.product_code_value = jsdata['product_code_value']
        self.publishers = jsdata['publishers']
        self.region = jsdata['region']
        self.release_date = jsdata['release_date']
        try :
            self.resolutions = jsdata['resolutions']
        except :
            self.resolutions = None
        try :
            self.singleplayer_features = jsdata['singleplayer_features']
        except :
            self.singleplayer_features = None
        try :
            self.sound_systems = jsdata['sound_systems']
        except :
            self.sound_systems = None
        self.widescreen_support = jsdata['widescreen_support']


class Review :

    def __init__(self, jsdata):

        self.api_detail_url = jsdata['api_detail_url']
        self.deck = jsdata['deck']
        self.description = jsdata['description']
        self.dlc_name = jsdata['dlc_name']
        self.game = jsdata['game']
        self.guid = jsdata['guid']
        self.id = jsdata['id']
        self.platforms = jsdata['platforms']
        self.publish_date = jsdata['publish_date']
        self.release = jsdata['release']
        self.reviewer = jsdata['reviewer']
        self.score = jsdata['score']
        self.site_detail_url = jsdata['site_detail_url']


class Theme :

    def __init__(self, jsdata):

        self.api_detail_url = jsdata['api_detail_url']
        self.guid = jsdata['guid']
        self.id = jsdata['id']
        self.name = jsdata['name']
        self.site_detail_url = jsdata['site_detail_url']


class UserReview :

    def __init__(self, jsdata):

        self.api_detail_url = jsdata['api_detail_url']
        self.date_added = jsdata['date_added']
        self.date_last_updated = jsdata['date_last_updated']
        self.deck = jsdata['deck']
        self.description = jsdata['description']
        self.game = jsdata['game']
        self.release = jsdata['release']
        self.dlc = jsdata['dlc']
        self.guid = jsdata['guid']
        self.id = jsdata['id']
        self.reviewer = jsdata['reviewer']
        self.score = jsdata['score']
        self.site_detail_url = jsdata['site_detail_url']

# This section has a lot of try / except blocks because search objects in the API
# Have the elements of the original item; I have to expect that the elements might
# not be there
class SearchObject :

    def __init__(self, jsdata):
        try : self.api_detail_url = jsdata['api_detail_url']
        except : self.api_detail_url = None
        try : self.date_added = jsdata['date_added']
        except : self.date_added = None
        try : self.date_last_updated = jsdata['date_last_updated']
        except : self.date_last_updated = None
        try : self.deck = jsdata['deck']
        except : self.deck = None
        try : self.description = jsdata['description']
        except : self.description = None
        try : self.guid = jsdata['guid']
        except : self.guid = None
        try : self.id = jsdata['id']
        except : self.id = None
        try : self.image_urls = jsdata['image']
        except : self.image_urls = None
        try : self.name = jsdata['name']
        except : self.name = None
        try : self.site_detail_url = jsdata['site_detail_url']
        except : self.site_detail_url = None
        self.resource_type = jsdata['resource_type']

class Type :

    def __init__(self, jsdata):

        self.detail_resource_name = jsdata['detail_resource_name']
        self.id = jsdata['id']
        self.list_resource_name = jsdata['list_resource_name']