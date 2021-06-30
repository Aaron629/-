from selenium import webdriver
driverPath = "C:\\Users\\haolun.DESKTOP-673FV82\\Downloads\\chromedriver_win32\\chromedriver.exe"
browser = webdriver.Chrome(driverPath)

url = "C:\\Users\\haolun.DESKTOP-673FV82\\Downloads\\TestHTML.html"
browser.get(url)

n1 = browser.find_elements_by_xpath('//h1')
print("所有課程名稱(xpath):")
for i in n1:
    print(i.text)
    
n2 = browser.find_elements_by_class_name('coursename')
print("所有課程名稱(classname):")
for i in n2:
    print(i.text)
    
n3 = browser.find_element_by_xpath('//section[4]//p')
print("新產品開發課程的時間:")
print(n3.text)

n4 = browser.find_elements_by_class_name('room')[1]
print("人工深度智慧學習的教室:")
print(n4.text)