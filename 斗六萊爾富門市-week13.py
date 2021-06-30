import requests
from bs4 import BeautifulSoup

def parse(soup):
    table = soup.find("div","searchResults")
    for i in table.find_all("tr"):
        print(i.find('a').text)
        
url="https://www.hilife.com.tw/storeInquiry_street.aspx"
session = requests.session()
resp = session.get(url)
soup = BeautifulSoup(resp.content, 'html.parser')

view_state = soup.find(id='__VIEWSTATE')['value']
event_validation = soup.find(id='__EVENTVALIDATION')['value']
viewstate_generator =soup.find(id='__VIEWSTATEGENERATOR')['value']

body1={
       "__EVENTTARGET":"CITY",
       "__EVENTARGUMENT":"",
       "__LASTFOCUS":"",
       "__VIEWSTATE":view_state,
       "__VIEWSTATEGENERATOR":event_validation,
       "__EVENTVALIDATION":event_validation,
       "CITY":"台北市",
       "AREA":"中正區"
       }

html=session.post(url,data=body1)
soup=BeautifulSoup(html.content,'html.parser')

view_state = soup.find(id='__VIEWSTATE')['value']
event_validation = soup.find(id='__EVENTVALIDATION')['value']
viewstate_generator =soup.find(id='__VIEWSTATEGENERATOR')['value']

body2={
       "__EVENTTARGET":"CITY",
       "__EVENTARGUMENT":"",
       "__LASTFOCUS":"",
       "__VIEWSTATE":view_state,
       "__VIEWSTATEGENERATOR":event_validation,
       "__EVENTVALIDATION":event_validation,
       "CITY":"雲林縣",
       "AREA":"斗六市"
       }

html=session.post(url,data=body2)
soup=BeautifulSoup(html.content,'html.parser')


print(soup.text)