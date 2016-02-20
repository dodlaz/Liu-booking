#!/usr/bin/python
import sys
import requests
from bs4 import BeautifulSoup

if len(sys.argv) != 3:
    sys.exit("You heve to add LIU-UserName and Password.")


# Login
#==================================================================
url="https://se.timeedit.net/web/liu/db1/timeedit/sso/?ssoserver=liu_stud_cas&entry=wr_stud&back=https%3A%2F%2Fse.timeedit.net%2Fweb%2Fliu%2Fdb1%2Fwr_stud%2Fri1Q8.html"
body = {'username':sys.argv[1], 'password':sys.argv[2]}
s = requests.Session()
loginPage = s.get(url)
soup = BeautifulSoup(loginPage.text)
cookies = dict(loginPage.cookies)
s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'

hiddenInputs = soup.findAll(name = 'input', type = 'hidden')
for hidden in hiddenInputs:
    name = hidden['name']
    value = hidden['value']
    body[name] = value
r = s.post(soup.form['action'], data = body, headers = {'Referer': url})
print(r)





# Booking
#=====================================================================
# URL to POST TO: https://se.timeedit.net/web/liu/db1/wr_stud/ri.html?h=t&sid=4
# RawData: kind=reserve&nocache=4&l=en&o=264465.195&o=278206.184&aos=&dates=20160220&starttime=7%3A00&endtime=8%3A00&url=https%3A%2F%2Fse.timeedit.net%2Fweb%2Fliu%2Fdb1%2Fwr_stud%2Fri1Q8.html%2300264465&fe7=


url="https://se.timeedit.net/web/liu/db1/wr_stud/ri.html?h=t&sid=4"
params = [
    ("kind", "reserve"),
    ("nocache", 4),
    ("l", "en"),
    ("o", 264465.195), #user or the room id
    ("o", 278206.184), #user or the room id
    ("aos", ""),
    ("dates", 20160220), #Date
    ("starttime", "7%3A00"), #StartTime
    ("endtime", "8%3A00"), #EndTime
    ("url", "https%3A%2F%2Fse.timeedit.net%2Fweb%2Fliu%2Fdb1%2Fwr_stud%2Fri1Q8.html%2300264465&fe7="),
]

res = requests.post(url=url,
                    data=params,
                    headers={'Content-Type': 'application/octet-stream'})
print(res)
