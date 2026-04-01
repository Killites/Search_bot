from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

wait = WebDriverWait(driver, 10)

# Open DuckDuckGo
driver.get("https://duckduckgo.com/")

# Find search box
search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))

# Type slowly (human-like)
search_box.send_keys("Python automation")
time.sleep(2)
search_box.send_keys(Keys.RETURN)

# Click first result
first_result = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "a.result__a"))
)

first_result.click()

time.sleep(5)
driver.quit()