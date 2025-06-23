from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

# Initialize driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open Instagram
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)

# Login credentials (Use dummy account)
USERNAME = "your_dummy_username"
PASSWORD = "your_dummy_password"

# Input username and password
driver.find_element(By.NAME, "username").send_keys(USERNAME)
driver.find_element(By.NAME, "password").send_keys(PASSWORD)
driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
time.sleep(7)

# Search for cbitosc
search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
search_box.send_keys("cbitosc")
time.sleep(3)
search_box.send_keys(Keys.RETURN)
time.sleep(2)
search_box.send_keys(Keys.RETURN)
time.sleep(5)

# Click Follow if not already following
try:
    follow_button = driver.find_element(By.XPATH, "//button[text()='Follow']")
    follow_button.click()
    print("Followed the account.")
except:
    print("Already following or button not found.")

time.sleep(5)

# Extract bio and stats
try:
    bio = driver.find_element(By.XPATH, "//div[contains(@class,'-vDIg')]/span").text
    stats = driver.find_elements(By.XPATH, "//ul[contains(@class,'k9GMp')]/li")

    posts = stats[0].text
    followers = stats[1].text
    following = stats[2].text

    data = f"CBIT OSC Instagram Page Data:\n\nBio:\n{bio}\n\n{posts}\n{followers}\n{following}"
    with open("cbitosc_info.txt", "w", encoding="utf-8") as file:
        file.write(data)

    print("Data extracted and saved to cbitosc_info.txt")

except Exception as e:
    print(f"Error extracting info: {e}")

# Close browser
driver.quit()
