import requests 
import sys
import json


''' check the legth of the command-line inputs, we want only 2 '''
if len(sys.argv) != 2:
    sys.exit() # exit if is not length 2
# making a request to the api    
res = requests.get("https://itunes.apple.com/search?entity=song$limit=5&term=" + sys.argv[1])
# printing the result boorring!
#print(json.dumps(res.json(), indent=2))

# from the response grab the object 'o'
#o = res.json()
print(res.content)
# for result in o["results"]:
    # print(result['trackName'])