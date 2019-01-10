from bs4 import BeautifulSoup
import urllib3
import requests
import os
import webbrowser

url = 'https://10fastfingers.com/typing-test/english'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')
p = soup.find('span',class_='highlight')

print(p)