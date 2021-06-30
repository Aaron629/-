from selenium import webdriver

driverPath = "C:\\Users\\haolun.DESKTOP-673FV82\\Downloads\\chromedriver_win32\\chromedriver.exe"
browser = webdriver.Chrome(driverPath)
print(type(browser))

url = 'https://www.yuntech.edu.tw/'
browser.get(url)

print('瀏覽器名稱 =',browser.name)
print('網頁標題 =',browser.title)
print('網頁原始碼 =',browser.page_source)
print('目前網址 =',browser.current_url)
print('網頁連線ID =',browser.session_id)
print('瀏覽器功能設定 = \n',browser.capabilities)

element = browser.find_element_by_link_text("行事曆")
element.click()

from time import sleep
sleep(10)
browser.close()
browser.quit()