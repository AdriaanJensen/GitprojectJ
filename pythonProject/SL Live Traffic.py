import json
import requests
import pprint
from datetime import datetime, timedelta
from datetime import date
from threading import Timer


date_today = date.today()  #Det här simpelt, bara se tiden som ett tidigt test till at skicka till homey
print("Today's date:", date_today) #    ^
time_now = datetime.now().strftime("%H:%M:%S") #    ^
print("the current time is", time_now)  #    ^

url1 = 'https://api.sl.se/api2/typeahead.json'  #Websidans/Stället där all info finns och jag måste hitta
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


url2 = 'https://api.sl.se/api2/typeahead.json'  #Websidans/Stället där all info finns och jag måste hitta
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



Variabel=datetime.today()
Stora_Variabel= Variabel.replace(day=Variabel.day, hour=6, minute=30, second=0, microsecond=0) + timedelta(days=1)
delta_t=Stora_Variabel-Variabel

sekunder=delta_t.total_seconds()

def hello_world():
    print("hello Samuel")
    #...

t = Timer(sekunder, hello_world)
t.start()


Traffic = 'https://api.sl.se/api2/deviations.json'  #Websidan/Stället där all info finns och jag måste hitta
params = {
    #"siteId": 9260,
    "siteId": 9702,  #Det här är "siteId" Idet för stationen som jag vill se infon om alltså Jakobsberg
    "key": 'YOUR_KEY_HERE',  #Key här
    "transportMode": 'train, bus'  #Vilka transport medel som jag vill ska visas, när jag letar efter problem
}
svar1 = requests.get(Traffic, params) #Calling Data from Trafiklabs
direktiv1 = svar1.json() #Turning Data into Json format
Homey_Data = []  #Här skapar jag en lista som all data som jag vill skicka till homey ska skickas hamnar här
#print(direktiv1) #checking Data returned

if "ResponseData" not in direktiv1:   #To check that if ResponseData not in what is returned then something has gone wrong
    print("Error: ResponseData not found in response")
else:
    for alert in direktiv1["ResponseData"]:    #If it has ResponseData in the data then it goes here to be narrowed down and fixed
        if alert["Header"] == "Inställd linje":  #Narrwos it down to only the Headers and the infowmation tied to them, which makes all the info in total much less.
            Homey_Data.append(alert)  #Adds all the info that we have reduced into the list that we made for Homey to use later
            print(json.dumps((Homey_Data)))  #Prints it so we may see the beauty of my creation
        if alert["Details"][0] == "Linje":  #Is supposed to do the same thing as Headers but with details as in what time and when where specifically it may affect the trains or busses
            Homey_Data.append(alert)  #same thing as before add it to the list
            print(json.dumps((Homey_Data)))  #Sadly i am not getting out the info i want from here, so that is a work in progress to find the correct key words
        if alert["ScopeElements"] == "Pendeltåg":  #Same problem as Details, but this one is supposed to only present what Pendeltåh linje the problem is affecting
            Homey_Data.append(alert)  #Same thing as the other 2 add info collected to the list
            print(json.dumps((Homey_Data)))  #is supposed to print the Pendeltåg linje but is currently refusing to do so.

                                         #I am able to print all the data that i get from Headers but the problem is that it is too much to say,
                                         #And Python does not support ÅÄÖ so that is a problem that needs to be fixed but not in this current moment

Homeyurl = "https://webhooks.athom.com/webhook/57274085acb3bd6d24b3d200/?token=irs8iS044k"  #Websidan till min egna personliga Homey där jag fårt infot jag skickar
Data = {
    "event": "Traffic",  #Namn av eventet
    "data1": str(date_today),  #Det jag skickar, alltså datumet som jag säger innnan
    "data2": originId,  #skickar de här också men de används inte
    "data3": destId   #skickar de här också men de används inte
}
requests.post(Homeyurl, data=json.dumps(Data), headers={"Content-Type": "application/json"})  #Det här är webhooken som används för att skicka det korrekt
                                                                                              #Och den måste i den här delen visa Datan som skickas och "Headers" alltså rubrik(men egentligen måste det vara det som står där


#if "StatusCode" in direktiv1 and direktiv1["StatusCode"] == 0: #if not 0 there are problems
    #print(" ")
    #storning1 = direktiv1["ResponseData"][0]["Header"][0]["Details"][0]
    #print(storning1)
    #for storning1 in storning1:
        #print(f"Type: {storning1['Scope']}, Message: {storning1['Message']}")
#else:
    #print("Inga störningar hittade")





     #All of this is is the vestige of what i wanted to do in the beginning but was actually just me going off the rails that my mother wanted me to follow
     #But i think i would want to finish this another time maybe so that it could maybe see some real use.
     #This part of the program actually fails but everything alse until this point is fine


Resa = 'https://api.sl.se/api2/TravelplannerV3_1/trip.<json>'  #Websidan/Stället där all info finns och jag måste hitta

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




             #There are some ideas that i would like to pursue after this project is handed in that i could not fit into the time frame
             #Like making a server that could keep the programm running without me having to dtart it
             #Using Docker and Linux and using NAS serversg








