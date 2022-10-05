#網路連線
import urllib.request as request 
import ssl
import json
ssl._create_default_https_context = ssl._create_unverified_context
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response)
infor = data["result"]["results"]
with open("data.csv", "w", encoding="utf-8") as file:
    for spot in infor:
        if (spot["xpostDate"] >= "2015"):
            urls = spot["file"].split("https://")   # urls 是 list
            file.write(spot["stitle"]+ "," + spot["address"][5:8] + "," + spot["longitude"] + "," + spot["latitude"] + "," + "https://" + urls[1] + "\n")





