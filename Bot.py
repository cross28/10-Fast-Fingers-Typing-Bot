from selenium import webdriver
from pynput.keyboard import Key, Controller
import time

siteurl = 'https://10fastfingers.com/typing-test/english'

keyboard = Controller()

choice = input('How many wpm would you like to type (Enter a number or the word max): ')

#Setting up test browser
driver = webdriver.Chrome()
driver.get(siteurl)
driver.implicitly_wait(15)

while True:
    word = driver.find_element_by_class_name('highlight')

    if (choice.upper() == 'MAX'):
        time.sleep(0)
    else:
        time.sleep(60/int(choice))

    for a in word.text:
        keyboard.press(a)
        keyboard.release(a)
    keyboard.press(' ')
    keyboard.release(' ')