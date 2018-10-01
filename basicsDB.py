import json
import requests

data = json.load(open("zipcodes.json"))

URL = "https://api.darksky.net/forecast/24f330227c3ef92be9f5428efb93ee75/"

enter = input("Enter a zip code: \n")

while enter not in data.keys():
    enter = input("Zipcode NOT valid, try another one \n")

with open("latNlong.txt","a") as LL:
    lat = data.get(enter)
    lat = lat[0] + "," + lat[1] + "\n"
    LL.writelines(lat)

URL = URL + data.get(enter)[0] + "," + data.get(enter)[1]

r = requests.get(url = URL)

#request has been sent and will be recieved

data = r.json()

lat = data.get('latitude')
long = data.get('longitude')
zone = data.get('timezone')
cur = data.get('currently')

print("latitude: " + str(lat))
print("longitude: " + str(long))
print("Timezone: " + zone)
for a in cur.keys():
    print(a + ": " +  str(cur.get(a)))
