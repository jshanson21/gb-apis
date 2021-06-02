import urllib.request, urllib.parse, urllib.error
import json


# Checks to see if there is a regToken available for the app.  The intent
# is that if there isn't, then the app should prompt the user to get
# a code and go through the authUser flow
def checkForRegToken() :
    # Tries to open up the file where the regToken will be stored by
    # other functions.  If the file doesn't exist, it will be created
    # and return False
    try : fh = open('regToken.txt','r')
    except : 
        fh = open('regToken.txt', 'w+')
        return False
    tmptext = fh.readline()
    # If the file is empty, return False; otherwise, assume that whatever
    # is there is the regToken (nothing else should be written to this file)
    if tmptext == '' : return False
    else : return True


# Takes in a 6-character code from http://www.giantbomb.com/app/myapp,
# submits it back to GB from within the App, and then receives back
# the api_key (in the form of a regToken) to use with API requests
def authUser(code) :
    url = 'http://www.giantbomb.com/app/myapp/get-result?regCode=' + code + '&format=json'
    data = urllib.request.urlopen(url).read()
    try :
        jsdata = json.loads(data)
    except :
        jsdata = None
    if jsdata is None or jsdata['status'] != 'success' or 'regToken' not in jsdata :
        print('regToken not received')
        return None
    return jsdata['regToken']


# Takes in the regToken obtained from authUser() and stores it in the
# text file
def storeToken(token) :
    fh = open('regToken.txt', 'w+')
    fh.write(token)


