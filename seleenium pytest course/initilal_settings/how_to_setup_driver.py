import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

#method 1
driver = webdriver.Chrome()

#method 2
#https://pypi.org/project/webdriver-manager/
#pip install webdriver-manager
#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Navigate to the login page
driver.get("https://beta.sproutsai.com/")

# Define login credentials
email = "pankaj+natera@sproutsai.com"
password = "Demo@123"

# Find the email and password input fields and submit button
email_field = driver.find_element("xpath", "//input[@type='email']")  # Replace "id" with the actual identifier of the email input field
password_field = driver.find_element("xpath", "//input[@type='password']")  # Replace "id" with the actual identifier of the password input field
submit_button = driver.find_element("xpath", "//button[@type='submit']")  # Replace "id" with the actual identifier of the submit button

# Enter email and password
# Enter email and password
email_field.send_keys(email)
password_field.send_keys(password)

# Submit the form
submit_button.click()

# Print cookies after login
print("Cookies after login:")
print(driver.get_cookies())

input()
