import sys
import requests

# yyyymmdd
dateInput = sys.argv[1]

url = "http://data.nba.net/data/10s/prod/v1/" + dateInput + "/scoreboard.json"
headers = {"Host": "data.nba.net"}
response = requests.get(url, headers=headers)
if response.status_code == requests.codes.ok:
    fh = open("game." + dateInput + ".json", "w")
    fh.write(response.content)
    fh.close()
