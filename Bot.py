from selenium import webdriver
from pynput.keyboard import Key, Controller
import time

siteurl = 'https://10fastfingers.com/typing-test/english'

keyboard = Controller()

#Setting up test browser
driver = webdriver.Chrome()
driver.get(siteurl)
driver.implicitly_wait(15)

while True:
    word = driver.find_element_by_class_name('highlight')

    for a in word.text:
        keyboard.press(a)
        keyboard.release(a)
    keyboard.press(' ')
    keyboard.release(' ')