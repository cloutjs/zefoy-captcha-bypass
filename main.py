from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.set_window_size(1920, 1080)
browser.get("https://zefoy.com/")
browser.add_cookie({"name": "PHPSESSID", "value": "paste your ssid here"})
browser.refresh()
time.sleep(30)
