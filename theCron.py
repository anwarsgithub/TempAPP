import requests

URL = "https://api.darksky.net/forecast/24f330227c3ef92be9f5428efb93ee75/"

with open("latNlong.txt", "r") as LL:
    LL = LL.read()
    LL = LL.splitlines()
    for l in LL:
        newURL = URL + l
        print(newURL)
