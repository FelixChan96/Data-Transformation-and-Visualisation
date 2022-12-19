import urllib.request

with urllib.request.urlopen("https://api.etherscan.io/api?module=account&action=balancemulti&address=0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a,0x63a9975ba31b0b9626b34300f7f627147df1f526,0x198ef1ec325a96cc354c7266a038be8b5c558f67&tag=latest&apikey=N6RXSV29BTHWDIX4Y3YVS78T1A2PPX7Y7I") as url:
    s = url.read()
    print(s)

     


