from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def click_when_clickable(driver, by, value, wait=10):
    try:
        WebDriverWait(driver, wait).until(EC.element_to_be_clickable((by, value))).click()
        time.sleep(0.5)
    except:
        pass

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1280,800")

driver = webdriver.Chrome(options=options)

driver.get("https://www.duolingo.com/")

# ✅ Insert your full Duolingo bot logic here
print("🚀 Running...")

time.sleep(5)

driver.quit()
