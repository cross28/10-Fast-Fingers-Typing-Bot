import webbrowser
from selenium import webdriver

siteurl = 'https://10fastfingers.com/typing-test/english'

#Setting up test browser
driver = webdriver.Chrome()
driver.get(siteurl)
driver.implicitly_wait(15)
pbutton = driver.find_element_by_class_name('highlight')
print(pbutton.text)

''' PERSONAL REFERENCE TO BEAUTIFUL SOUP AND REQUESTS

from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq

#connecting to page and parsing
site = uReq(siteurl)
site_html = site.read()
soup = BeautifulSoup(site_html, 'html.parser')

print(soup.findAll('span',{'class':'highlight'}))
'''