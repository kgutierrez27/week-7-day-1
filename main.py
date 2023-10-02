#working with apis and dictionaries
import requests
import json
response=requests.get("https://randomuser.me/api")
#print(response.json())
title=response.json()['results'][0]['name']['first']
response.json()['results'][0]['name']['first']
gender=response.json()['results'][0]['gender']
lname=response.json()['results'][0]['name']['last']
city=response.json()['results'][0]['location']['city']
country=response.json()['results'][0]['location']['country']
state=response.json()['results'][0]['location']['state']
email=response.json()['results'][0]['email']
usern=response.json()['results'][0]['login']['username']
passw=response.json()['results'][0]['login']['password']
print(gender)
print(title)
print(lname)
print(city)
print(country)
print(state)
print(email)
print(usern)
print(passw)