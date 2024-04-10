import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://telephonycloud.co.in/portal/")
link = driver.find_element_by_link_text('Imarticus Learning Pvt Ltd - VB')
link.click()







