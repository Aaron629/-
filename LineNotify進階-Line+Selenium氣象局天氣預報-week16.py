from selenium import webdriver
from time import sleep
import requests

driverPath = "C:\\Users\\haolun.DESKTOP-673FV82\\Downloads\\chromedriver.exe"
browser = webdriver.Chrome(driverPath)

token = 'cm1GDyiLRyfDeZMzpnQxblvuVnI3knoSr3EnccmzLE8'

url = 'https://www.cwb.gov.tw/V8/C/'
def meteorological():
    browser.get(url)
    browser.maximize_window()
    
    township = browser.find_element_by_class_name('forecast-township-title')
    township.click()
    sleep(3)
    
    city = browser.find_element_by_partial_link_text('雲林縣')
    city.click()
    sleep(3)
    
    area = browser.find_element_by_partial_link_text('斗六市')
    area.click()
    sleep(3)
    
    hr3 = browser.find_element_by_id('Tab_3hr')
    hr3.click()
    sleep(3)
    
    table = browser.find_element_by_class_name('table-responsive')
    browser.execute_script('var q=document.documentElement.scrollTop='+str(int(table.rect['y'])))
    browser.execute_script('var q=document.documentElement.scrollTop='+str(int(table.rect['x'])))
    table.screenshot('./cap_wheather.png')
    
def lineNotifyMessage_image(token, image_path):
    headers = {
        "Authorization":"Bearer " + token,
    }
    
    files = {'imageFile' :open(image_path, 'rb')}
    payload = {'message': '雲林斗六氣象預報' }
    r = requests.post("https://notify-api.line.me/api/notify",
                         headers = headers, params=payload, files=files)
    print(r.status_code)
    return r.status_code

image_path = r'./cap_wheather.png'
meteorological()
lineNotifyMessage_image(token, image_path)
    
   
