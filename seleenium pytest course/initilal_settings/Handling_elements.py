#how to select the elements

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.wheel_actions import WheelActions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


#id,name,tagname,linktext,partial linktext,tagname,css,xpath

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
Waiting_time = WebDriverWait(driver,10)


#id
driver.get('https://images.google.com/')

box = Waiting_time.until(EC.element_to_be_clickable((By.ID,'APjFqb')))

actions = ActionChains(driver)
actions.move_to_element(box).click().key_down(Keys.SHIFT).send_keys('amara lingeshwara kona tirupati').key_up(Keys.SHIFT).perform()
actions.send_keys(Keys.ENTER).perform()


#box.send_keys('amara lingeshwara kona tirupati')
#
#search = Waiting_time.until(EC.element_to_be_clickable((By.XPATH, "//button[@jsname='Tg7LZd' and @class='Tg7LZd']" )))
#search.click()

input()

#
##name
#image_main_box = Waiting_time.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@jsname ='r5xl4']/div")))
#print(len(image_main_box))
##all_images = driver.find_elements(By.XPATH, "//div[@data-ved=\"2ahUKEwjLnePko9-CAxWkXmwGHUWLC_YQMygAegQIARBE\"]")
##
#j=0
#for i in image_main_box:
#
#    j+=1
#    clicked = WebDriverWait(i,10).until(EC.element_to_be_clickable((By.XPATH, f'//div[@jsname =\'r5xl4\']/div[{j}]')))
#    clicked.click()
#
#input()

#driver.get('https://www.btrkona.online/')
#box = Waiting_time.until(EC.element_to_be_clickable((By.XPATH,'//*[contains(text(), "Youtube")]')))
#box.click()
#text = Waiting_time.until(EC.presence_of_element_located((By.XPATH,'//main/p')))
#print(text.text)
# Locate the element to which you want to scroll (or just use the body element)

#element_to_scroll = driver.find_element(By.TAG_NAME,"body")

# Create an ActionChains object
#actions = ActionChains(driver)

# Perform a wheel action (scroll down)
##actions.move_to_element(element_to_scroll).send_keys(Keys.ARROW_DOWN).perform()

#time.sleep(5)
#element_to_scroll_to = driver.find_element(By.XPATH,"//div/div/div/h2[@class='post-title']")
#script = f"arguments[0].scrollIntoView();"
#driver.execute_script(script, element_to_scroll_to)



#input()