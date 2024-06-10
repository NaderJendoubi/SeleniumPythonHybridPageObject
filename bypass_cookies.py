import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.opera.com/fr/download")
driver.maximize_window()

time.sleep(2)
driver.find_element(By.XPATH, "//span[text()='Accepter tout']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='header__download']").click()

driver.quit()