#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import WebDriverException as WebDriverException

options = webdriver.ChromeOptions()
options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" 
chrome_driver_binary = "C:\Webdriver\chromedriver"
driver = webdriver.Chrome(chrome_driver_binary, options=options) 

driver.get('https://web.whatsapp.com/')

name=input("Enter the name of user or group") 
msg = input("Enter your message") 
count = int(input("Enter the count"))

input("Enter anything after scanning QR code") 
input_box = driver.find_element(By.XPATH, '//*[@id="main"]//footer//div[contains(@shekhar, "true")]')
#driver.find_element_by_xpath('//span[@title= "{}"]'.format(name)).click()
#user = driver.find_element_by_xpath('//span[@_19RFN = "{}"]'.format(name))
#user.click()
msg_box = driver.find_element_by_class_name('_3u328')
for i in range(count) : 
    msg_box.send_keys(msg) 
    button = driver.find_element_by_class_name('_3M-N-') 
    button.click()


# In[ ]:




