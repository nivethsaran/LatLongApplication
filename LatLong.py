from bs4 import BeautifulSoup
import requests
import json
import urllib.parse,urllib.request
location=input('Enter Location:\n');
locact=location.split(" ")
namel=""
for name in locact:
    namel=namel+name
url="https://maps.googleapis.com/maps/api/geocode/json?key=<add_key_here>8&address="+namel
try:
    page=requests.get(url)
    soup=BeautifulSoup(page.content,'html.parser')
    sr=page.json()
    uh=urllib.request.urlopen(url)
    ac=uh.read().decode()
    js=json.loads(ac)
    print("Collecting data from server")
    
    if(js["status"]=="OK"):
        try:
            lat=js["results"][0]["geometry"]["location"]["lat"]
            print("Latitude:",lat)
            lon=js["results"][0]["geometry"]["location"]["lng"]
            print("Longitude:",lon)
        except:
            print("Place doesnt exist")
except:
    print("Check Your internet connection")



    
