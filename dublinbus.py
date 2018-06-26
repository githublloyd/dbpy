import urllib2
import json
import datetime
import time

url = 'https://data.smartdublin.ie/cgi-bin/rtpi/realtimebusinformation?stopid=381&routeid=1&format=json'

json_obj = urllib2.urlopen(url)

data = json.load(json_obj)

print("The date and time is " + data['timestamp'])
print("Your stop number is " + data['stopid'])

for item in data['results']:
 print("The next #1 bus is coming in (minutes) " + item['duetime'])
