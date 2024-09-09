import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1])

#the result of response.json() is stored in o
o = response.json()
# iterating through the results in o and printing each trackName
for result in o["results"]:
    print(result["trackName"])