import requests
import json

#establishing a secure connection: 
url = "https://api.data.abs.gov.au/data/C21_G09_SAL/all"
response = requests.get(url,timeout=1000000)
data = response.json()
print(response)
 