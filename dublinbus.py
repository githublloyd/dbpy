import urllib2
import json
import datetime
import time

url1 = 'https://data.smartdublin.ie/cgi-bin/rtpi/realtimebusinformation?stopid=381&routeid=1&format=json'
url2 = 'https://data.smartdublin.ie/cgi-bin/rtpi/realtimebusinformation?stopid=271&routeid=1&format=json'

json_obj1 = urllib2.urlopen(url1)
json_obj2 = urllib2.urlopen(url2)

data1 = json.load(json_obj1)
data2 = json.load(json_obj2)

### leaving Sandymount ###
print('The date and time is ' + data1['timestamp'])
print("\n")
print("Your stop number is " + data1['stopid'] + " (Park Avenue, St. john's Church)")
for item in data1['results']:
 print("The next #1 bus is coming in " + item['duetime'] + " minutes")
print("\n")
### leaving O'Connell St. ###
print("Your stop number is " + data2['stopid'] + " (O'Connell St., Abbey St.)")
for item in data2['results']:
 print("The next #1 bus is coming in " + item['duetime'] + " minutes")
