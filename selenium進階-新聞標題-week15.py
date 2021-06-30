from selenium import webdriver


driverPath = "C:\\Users\\haolun.DESKTOP-673FV82\\Downloads\\chromedriver.exe"
browser = webdriver.Chrome(driverPath)

url = 'https://news.ltn.com.tw/list/breakingnews/popular'
browser.get(url)

links = browser.find_elements_by_xpath('//ul[@class="list"]/li/a[@class="tit"]')
for link in links:
    print(link.get_attribute("title"))
# browser.quit();