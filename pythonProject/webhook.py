import requests
import json
webhook_url = "https://webhook.site/014ede3f-3bb0-4991-b596-c26f22c87d7a"
data = {" name" : "Lukas"}
requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})