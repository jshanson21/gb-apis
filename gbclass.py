import urllib.request, urllib.parse, urllib.error
import json
#import re

#Initiates a parameters dictionary to be used for the urls that has the parameters
#that every function would use; is called by the functions below
#THE API_KEY NEEDS TO BE UPDATED WITH YOUR API KEY
def initParams() :
    params = dict()
    params['api_key'] = '6da2f5489cc2a154ca0ea4b461b0376d49d442a4'
    params['format'] = 'json'
    return(params)

def loadData(url, params, errorMessage) :
    url = url + urllib.parse.urlencode(params)
    data = urllib.request.urlopen(url).read()
    try :
        jsdata = json.loads(data)
    except :
        jsdata = None
    if jsdata is None or "error" not in jsdata or jsdata["error"] != "OK" :
        print(errorMessage)
    return jsdata


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
    params['filter'] = ''
    for field in filters :
        params['filter'] = params['filter'] + field + ':' + filters[field] + ','
    return loadData(url, params, '===Could Not Retrieve Any Accessories===')

#Returns the json object for a game in the wiki based on the key (a string)
def getGame(key) :
    url = 'https://www.giantbomb.com/api/game/' + key + '/?'
    params = initParams()
    return loadData(url, params, '===Could Not Retrieve Game===')


#Returns the json-formatted contents of a search; the query is in the format of
#a string
def search(query) :
    url = 'https://www.giantbomb.com/api/search/?'
    params = initParams()
    params['query'] = query
    return loadData(url, params, '===Search error or no results found===')
