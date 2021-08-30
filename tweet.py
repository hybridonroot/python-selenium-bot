#hybridoitc
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

print('Debug Level 1')

URL = 'https://twitter.com/login'
print('Debug Level 2')

# User Name and Password to the twitter account
userUsername = 'twitter user name'
userPassword = 'password'
print('Debug Level 3')

# Message of a tweet with your key words
tweetMessage = 'twitter msg and tags'
print('Debug Level 4')

# Instantiate the webdriver with the executable location of MS Edge web driver Stored in HYBRIDOITC folders
browser = webdriver.Edge('path\msedgedriver.exe')
print('Debug Level 5')

# Opening Edge browser and navigating to the given URL #Twitter
browser.get(URL)
print('Debug Level 6')

# Browser Load Wait 
browser.implicitly_wait(5)
browser.maximize_window
print('Config Complete Opening Browser')

# Finding username and password field from the login page and save as follow

userInput = browser.find_element_by_name('session[username_or_email]')
passwordInput = browser.find_element_by_name('session[password]')

# Input username and password field from the var gen. & Login
userInput.send_keys(userUsername)
passwordInput.send_keys(userPassword)
passwordInput.send_keys(Keys.ENTER)

print('Sending Login Keys')

# Page Load Wait
browser.implicitly_wait(5)

# Loop To Repeat
print('Starting Tweet Loop')
for x in range(5000):
    time.sleep(5)
    tweet = browser.find_element_by_css_selector("br[data-text='true']")
    tweet.send_keys(tweetMessage)
    #to identify element File upload
    s = browser.find_element_by_xpath("//input[@type='file']")
    #file path specified with send_keys
    #
    s.send_keys("path_to_images")
    print('Message Send')
    button = browser.find_element_by_css_selector("div[data-testid='tweetButtonInline']")
    button.click()


time.sleep(2)
browser.close() 
print('finished')
