import requests
import json

#establishing a secure connection: 

response = requests.get("https://api.data.abs.gov.au/data/ABS,C21_G13_SAL,1.0.0/...10891..?startPeriod=2021&dimensionAtObservation=AllDimensions").json()
print(response.status_code)   
 
#Retrieving sample data from API:

data = response.text

#Parse the sample data into JSON format: 

parse_json = json.loads(data)

#print the sample data: 

print(parse_json) 