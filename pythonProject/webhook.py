import requests
import json
webhook_url = "https://webhook.site/d8c79cfd-d149-4ec4-8cdb-967fcfa05ad4"
data = {" name" : "Lukas"}
requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})

Homeyurl = "https://webhooks.athom.com/webhook/57274085acb3bd6d24b3d200/?token=irs8iS044k"
Data = {
    "event": "Traffic",
    "data1": "Train",
    "data2": "5794",
    "data3": "9114"
}

requests.post(Homeyurl, data=json.dumps(Data), headers={"Content-Type": "application/json"})
