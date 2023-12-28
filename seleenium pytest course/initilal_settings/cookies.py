from selenium import webdriver
import time
import pickle


driver = webdriver.Chrome()


driver.get("https://beta.sproutsai.com/")
cookies = pickle.load(open("cookies.pkl", "rb"))

for cookie in cookies:
    cookie['domain'] = ".sproutsai.com"
    
    try:
        driver.add_cookie(cookie)
    except Exception as e:
        print(e)

time.sleep(5)

driver.get("https://beta.sproutsai.com/")

input()