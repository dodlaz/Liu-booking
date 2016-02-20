#!/usr/bin/python
import sys
import requests
from bs4 import BeautifulSoup

if len(sys.argv) != 3:
    sys.exit("You heve to add LIU-UserName and Password.")


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
