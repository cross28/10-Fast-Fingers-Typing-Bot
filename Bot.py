from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import os
import json
import webbrowser

siteurl = 'https://10fastfingers.com/typing-test/english'

#connecting to page
site = uReq(siteurl)
site_html = site.read()

soup = BeautifulSoup(site_html, 'html.parser')
print(soup.findAll('div',{'id':'ow1'}))