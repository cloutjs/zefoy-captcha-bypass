from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
import time

browser = webdriver.Chrome()
browser.set_window_size(1920, 1080)
browser.get("https://zefoy.com/ ")
browser.add_cookie({"name": "PHPSESSID", "value": "6m13oeakatc26jtrb4pnko1054"})
browser.refresh()
time.sleep(30)