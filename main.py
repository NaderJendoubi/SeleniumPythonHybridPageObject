import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.amazon.fr/gp/bestsellers/electronics/ref=zg_bs_electronics_sm")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='sp-cc-accept']").click()

time.sleep(5)

elements = (WebDriverWait(driver, 10).
            until(EC.presence_of_all_elements_located((By.XPATH, "//div[@id='gridItemRoot']//span/div"))))

#elements = driver.find_elements(By.XPATH, "//div[@id='gridItemRoot']//a[2]//div")
print(len(elements))

for element in elements:
    print(element.get_attribute("textContent"))


driver.quit()
