#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

user = "st2021"
pwd = "allagrande"

driver = webdriver.Firefox()
driver.get("https://vati.it")

elem = driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div/div/a").click()
elem = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[1]/div/form/fieldset/div[1]/div/div/input")
elem.send_keys(user)
elem.send_keys(Keys.RETURN)
elem2= driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[1]/div/form/fieldset/div[2]/div/div/input")
elem2.send_keys(pwd)
elem2.send_keys(Keys.RETURN)
time.sleep(6)
elem3 = driver.find_element_by_xpath("/html/body/div/div/div/div/div[4]/ul/li[3]/a").click()
time.sleep(3)
elem4 = driver.find_element_by_xpath("/html/body/div/div/div/main/div[2]/div/div[2]/ul[1]/li[5]/a").click()
