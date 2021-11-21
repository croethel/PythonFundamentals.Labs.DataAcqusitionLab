import requests
import os
import json
from dotenv import load_dotenv


load_dotenv()


# query = {'lat': '45', 'lon': '180'}
# response = requests.get('http://api.open-notify.org', params = query)
# print(response.json())
#
# print(response.headers["date"])


my_headers = {'Token': os.getenv('api_key'),
              'Accept': '*/*',
              'Accept-Encoding': 'gzip, deflate, br',
              'Connection': 'keep-alive',
              'Content-Type': 'application/json'
              }

file_number = 0

for i in range(1, 38859, 1000):
    response = requests.get(f"https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?offset={i}&limit=1000", headers=my_headers)
    data = json.loads(response.text)

    with open(f"locations_{file_number}.json", "w") as f:
        f.write(json.dumps(data))
    file_number +=1

