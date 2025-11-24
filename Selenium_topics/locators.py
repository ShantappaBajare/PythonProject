import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

serv_obj= Service("C:/Users/Shantappa Bajare/PycharmProjects/PythonProject/Edge driver/msedgedriver.exe")
driver= webdriver.Edge(service=serv_obj)
driver.get("https://www.youtube.com/")
driver.maximize_window()

driver.find_element(By.XPATH,"//*[@id='center']/yt-searchbox/div[1]/form/input").send_keys("python Automation")
driver.find_element(By.XPATH,"//*[@id='center']/yt-searchbox/button/span/span/div").click()

time.sleep(10)
