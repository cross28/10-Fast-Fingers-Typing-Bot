from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import os
import webbrowser

siteurl = 'https://10fastfingers.com/typing-test/english'

#connecting to page
site = uReq(siteurl)
site_html = site.read()
site.close()
print(site_html)
soup = BeautifulSoup(site_html, 'html.parser')


