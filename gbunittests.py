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

#Unit test for getGame() function
print("TESTING GETGAME()")
tmpgame = gbclass.getGame('3030-12300')
print(tmpgame["results"]["name"])
print(tmpgame["results"]["description"])
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
