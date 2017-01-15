import json

import requests

url = "http://stats.nba.com/data/10s/v2015/json/mobile_teams/nba/2016/league/00_full_schedule.json"
headers = {"Host": "data.nba.com"}
response = requests.get(url, headers=headers)
if response.status_code == requests.codes.ok:
    print response.content