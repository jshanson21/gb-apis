import auth
import gbwiki as gb

# As prep:
#   1. If regToken.txt exists, delete it
#   2. Get a code from https://www.giantbomb.com/app/myapp/

# Checks whether the regToken exists
tmpbool = auth.checkForRegToken()
print(tmpbool)

# Enter in the code from the myapp website
code = '8BF4B2'
print(code)

# Gets the token by exchanging it for the code
regToken = auth.getToken(code)
print(regToken)

# Stores the token in a text file
auth.storeToken(regToken)

# Checks whether the regToken exists (should be True)
tmpbool = auth.checkForRegToken()
print(tmpbool)

# Retrieves the token
check = gb.getToken()
print(check)

# Runs a GB wiki request using the retrieved token instead of a
# hard-coded one
results = gb.getGame('3030-1')
print(results.name)
print(results.deck)

