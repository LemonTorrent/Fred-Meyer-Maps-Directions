
#C:\Program Files (x86)
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
# print(main.text)

time.sleep(1)

lenMain = int((len(main) - 3) / 5)
print("main", len(main))

time.sleep(1)

# for i in range(4, lenMain):
#     print(main[(i * 5) + 3].text)

# for i in range(len(main)):
#     print(main[i].aria_role)

links = [elem.get_attribute('href') for elem in main]
# print(links)
driver.get(links[0])

directions = driver.find_elements(By.CSS_SELECTOR, "[aria-label=Directions to Fred Meyer]")
print(directions)

time.sleep(10)

driver.quit()