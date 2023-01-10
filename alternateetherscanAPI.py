import urllib.request

with urllib.request.urlopen("https://api.data.abs.gov.au/data/ABS,C21_G13_SAL,1.0.0/...10891..?startPeriod=2021&dimensionAtObservation=AllDimensions") as url:
    s = url.read()
    print(s)

import json

if response.status_code == 200:
  data = response.json()
  with open('testABS.json','w') as f:
    json.dump(data,f, indent=2)

else:
  print('Failed to load data from API')

     


