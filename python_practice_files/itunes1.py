#JSON library that can help us interpret the data received
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
#json.dumps is implemented such that it utilizes indent to make the output more readable
print(json.dumps(response.json(), indent=2))