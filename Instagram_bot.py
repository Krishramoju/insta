from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def automate_instagram_search_and_follow():
    """
    Automates the process of logging into Instagram, searching for cbitosc,
    and following the account, while extracting data into a text file.
    """

    # --- Replace with your dummy account credentials ---
    username = "your_dummy_username"
    password = "your_dummy_password"

    # --- Initialize the webdriver (Chrome in this example) ---
    driver = webdriver.Chrome()  # You might need to specify the path to your chromedriver
    driver.get("https://www.instagram.com/")

    try:
        # --- Login ---
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        ).send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()


        # --- Handle "Save Your Login Info?" popup ---
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Not Now']"))
        ).click()

        # --- Handle "Turn on Notifications?" popup ---
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Not Now']"))
        ).click()

        # --- Search for cbitosc ---
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']"))
        )
        search_box.send_keys("cbitosc")
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)  # Allow time for search results to load

        # --- Select the first search result (cbitosc) ---
        first_result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/cbitosc/')]"))
        )
        first_result.click()

        # --- Follow cbitosc ---
        follow_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Follow']"))
        )
        follow_button.click()

        # --- Extract data (example: post count) ---
        time.sleep(2) # Wait for the page to load with the data
        post_count_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='_ac2a']"))
        )
        post_count = post_count_element.text
        print(f"Post count: {post_count}")

        # --- Save extracted data to a text file ---
        with open("cbitosc_data.txt", "w") as f:
            f.write(f"Post Count: {post_count}\n")
        
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # --- Close the browser ---
        driver.quit()



if __name__ == "__main__":
    automate_instagram_search_and_follow()
