import webbrowser
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
from selenium import webdriver
from pynput.keyboard import Key, Controller
import pynput.mouse as pymouse
import time

siteurl = 'https://10fastfingers.com/typing-test/english'

keyboard = Controller()
mouse = pymouse.Controller()

#Setting up test browser
driver = webdriver.Chrome()
driver.get(siteurl)
driver.implicitly_wait(15)

#Getting html data
siteReq = uReq(siteurl)
site = siteReq.read()
soup = BeautifulSoup(site, 'html.parser')

inputField = soup.findAll('span',{'class':'inputfield'})
word = driver.find_element_by_class_name('highlight')

time.sleep(3)
while True:
    soup.
    for a in word.text:
        keyboard.press(a)
        keyboard.release(a)
        time.sleep(0.05)
    keyboard.press(' ')
    time.sleep(.1)

''' PERSONAL REFERENCE TO BEAUTIFUL SOUP AND REQUESTS

from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq

#connecting to page and parsing
site = uReq(siteurl)
site_html = site.read()
soup = BeautifulSoup(site_html, 'html.parser')

print(soup.findAll('span',{'class':'highlight'}))
'''