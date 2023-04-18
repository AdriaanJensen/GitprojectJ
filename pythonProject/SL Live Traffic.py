import json
import requests
import pprint
from datetime import datetime
from datetime import date

date_today = date.today()
print("Today's date:", date_today)
time_now = datetime.now().strftime("%H:%M:%S")
print("the current time is", time_now)

url1 = 'https://api.sl.se/api2/typeahead.json'
parametrar1 = {
    'key': 'YOUR_KEY_HERE',
    #'searchstring': 'Däckelvägen', #namnet på platsen eller stationen/hållplatsen som ska skannas
    'searchstring': 'Jakobsberg_station', #namnet på platsen eller stationen/hållplatsen som ska skannas
    'stationsonly': 'True', #Lägg falsk om du vill kunna se hållplatser och addresser
}
Svar1 = requests.get(url1, parametrar1) #frågan efter API informationen
Info1 = Svar1.json() #Få datan som Json för att kunna läsa
resultat1 = Info1['ResponseData'][0] #Få det första resultatet på datan
originId = resultat1['SiteId'] #Faktiskt få Id till hållplatsen
print(originId) #print


url2 = 'https://api.sl.se/api2/typeahead.json'
parametrar2 = {
    'key': 'YOUR_KEY_HERE',
    'searchstring': 'Fridhemsplan', #namnet på platsen eller stationen/hållplatsen som ska skannas
    'stationsonly': 'True', #Lägg falsk om du vill kunna se hållplatser
}
Svar2 = requests.get(url1, parametrar2) #frågan efter API informationen
Info2 = Svar2.json() #Få datan som Json för att kunna läsa
resultat2 = Info2['ResponseData'][0] #Få det första resultatet på datan
destId = resultat2['SiteId'] #Faktiskt få Id till hållplatsen
print(destId) #print



Homeyurl = "https://webhooks.athom.com/webhook/57274085acb3bd6d24b3d200/?token=irs8iS044k"
Data = {
    "event": "Traffic",
    "data1": str(date_today),
    "data2": originId,
    "data3": destId
}
requests.post(Homeyurl, data=json.dumps(Data), headers={"Content-Type": "application/json"})


Traffic = 'https://api.sl.se/api2/deviations.json'
params = {
    #"siteId": 9260,
    "siteId": 9702,
    "key": 'YOUR_KEY_HERE',
    "transportMode": 'train, bus'
}
svar1 = requests.get(Traffic, params) #Calling Data from Trafiklabs
direktiv1 = svar1.json() #Turning Data into Json format
print(direktiv1) #checking Data returned
if "StatusCode" in direktiv1 and direktiv1["StatusCode"] != 0: #if not 0 there are problems
    storning1 = direktiv1["ResponseData"]["TrafficTypes"][0]["Deviations"]
    for storning1 in storning1:
        print(f"Type: {storning1['Scope']}, Message: {storning1['Message']}")
else:
    print("Inga störningar hittade")



Resa = 'https://api.sl.se/api2/TravelplannerV3_1/trip.<json>'

Params = {
    'key': 'YOUR_KEY_HERE',
    'originId': '5784',
    'destId': '9115',
    'searchForArrival': '0',
    'time': '2023-04-15T09:30:00',
    #'time': date_today+time_now,
    'products': 'BUS,TRAIN,METRO,TRAM,SHIP',
}
print(Params)

Response = requests.get(Resa, Params)
print(Response)

if Response.status_code == 200:
    data = Response.json()
    if 'Trip' in data and data['Trip']:
        result = data['Trip'][0]
        departure_time = result['LegList']['Leg'][0]['Origin']['time']
        arrival_time = result['LegList']['Leg'][-1]['Destination']['time']
        print(f"Departure time: {departure_time}")
        print(f"Arrival time: {arrival_time}")
    else:
        print("No results found.")
else:
    print(f"Error {Response.status_code}: {Response.reason}")

Information = Response.json()
print(Information)
Result = Information['Trip'][0]
avGangsTid = Result['Leglist']['Leg'][0]['Origin']['Tid']
anKomstTid = Result['Leglist']['Leg'][-1]['Destination']['Tid']
print(f"Departute time: {avGangsTid}")
print(f"Arrival time: {anKomstTid}")








