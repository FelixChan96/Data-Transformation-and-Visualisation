import urllib.request

with urllib.request.urlopen("https://api.data.abs.gov.au/data/ABS,C21_G13_SAL,1.0.0/...10891..?startPeriod=2021&dimensionAtObservation=AllDimensions") as url:
    s = url.read()
    print(s)

     


