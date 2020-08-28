from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd
import pyautogui

optionss = webdriver.ChromeOptions()
optionss.add_argument('--user-agent=Chrome/84.0.4147.89 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')

#optionss.binary_location = '/Users/divith/Documents/chromedriver' # Directory where your chrome.exe is, if it's not located automatically uncomment this line
chrome_driver_binary = '' # Change this to your own chromedriver path! 
webdriver = webdriver.Chrome(executable_path=chrome_driver_binary, options=optionss)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('yourUsernameHere')                  # Enter your username here
password = webdriver.find_element_by_name('password')
password.send_keys('yourPasswordHere')                  # Enter your password here

button_login = webdriver.find_element_by_xpath('//button[normalize-space()="Log In"]')
webdriver.execute_script("arguments[0].click();", button_login)
sleep(5)

notnow = webdriver.find_element_by_xpath('//button[normalize-space()="Not Now"]')
notnow.click() #comment out this section, if you don't get a pop up asking about notifications
sleep(4)

try:
    cancel = webdriver.find_element_by_xpath('//button[normalize-space()="Cancel"]') #Sometimes a pop-up asking you to add Instagram to home screen comes on. Leave this be, as it will
    cancel.click() 
    sleep(4)
except:
    pass

try:
    notnow = webdriver.find_element_by_xpath('//button[normalize-space()="Not Now"]') # Idk why I added this section but hey my code now has 69 lines
    notnow.click() 
    sleep(4)    
except:
    pass


newP = webdriver.find_elements_by_xpath("//div[@data-testid='new-post-button']") # The button for uploading posts!
newP[0].click()
sleep(2)


pyautogui.write('/Users/div/Downloads/pikachu.png')  # This is the location to your photo that you wanna upload.
sleep(1)        
pyautogui.press('return')
sleep(2)            #  If you're gonna be uploading videos I reccommend setting the sleep(x) value of x to a higher value so it uploads

next1 = webdriver.find_element_by_xpath('//button[normalize-space()="Next"]')
next1.click()
sleep(2)

txt = webdriver.find_element_by_class_name('NfvXc') # This is the box where you write your post caption
txt.send_keys('')
txt = webdriver.find_element_by_class_name('NfvXc')
txt.send_keys('test') # Descrition/Caption here!
txt.send_keys(Keys.ENTER)
sleep(2)

shaer = webdriver.find_element_by_xpath('//button[normalize-space()="Share"]') # Final click on share button and you're good to go
shaer.click()
sleep(4)