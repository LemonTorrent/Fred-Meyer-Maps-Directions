
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def launchBrowser():
    # How to use path with updated version of selenium, but not needed
    # PATH = "C:\Program Files (x86)\chromedriver.exe"
    # service = Service(executable_path="C:\Program Files (x86)\chromedriver.exe")
    # options = webdriver.ChromeOptions()
    # driver = webdriver.Chrome(service=service, options=options)

    
    driver.get("https://www.google.com/maps/@45.4950912,-122.6147085,14z?entry=ttu")

    print(driver.title)

    time.sleep(1)

    

launchBrowser()

search = driver.find_element("name", "q")
search.send_keys("Fred Meyer")
search.send_keys(Keys.RETURN)

time.sleep(2)

main = driver.find_elements(By.CLASS_NAME, "hfpxzc")

time.sleep(1)

lenMain = int((len(main) - 3) / 5)
print("main", len(main))

time.sleep(1)

links = [elem.get_attribute('href') for elem in main]
driver.get(links[0])

directions = driver.find_element(By.CSS_SELECTOR, "[aria-label='Directions to Fred Meyer']")
print(directions)
directions.click()

time.sleep(2)

directionsStart = driver.find_element(By.ID, "section-directions-trip-0")
directionsStart.click()

time.sleep(10)

driver.quit()