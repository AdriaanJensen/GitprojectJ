import json
import requests
import pprint


#url = 'https://api.sl.se/api2/LineData.json?model=[https://api.sl.se/api2/LineData]&key=[KEY]'
#r = requests.get(url)


#Trip = 'https://api.sl.se/api2/TravelplannerV3_1/trip.<json>?key=<KEY>¶metrar'
#Trip = 'https://api.sl.se/api2/TravelplannerV3_1'

TestApi = "https://api.tvmaze.com/singlesearch/shows"
Params = {"q":"girls"}
response1 = requests.get(TestApi, Params)

if response1.status_code == 200:
    data = json.loads(response1.text)
    pprint.pprint(data)
else:
    print(f"Error: {response1.status_code}")

word = input("what word would you like to translate?")
url = 'https://christianthompson.com/dictionary.py?'

params = {"word":word}
response = requests.get(url, params)

print(f"Status Code: {response.status_code}")

print(response.text)


















