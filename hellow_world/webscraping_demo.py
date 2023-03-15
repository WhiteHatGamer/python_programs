import re
import sys,time,requests
from bs4 import BeautifulSoup
count=0
url = "https://www.cricbuzz.com"
try:
    page=requests.get(url)
    #page=requests.get("http://www.rediff.com")
except Exception as e:
    error_type,error_obj, error_info = sys.exc_info()
    print("Error for Links",url)
    print(error_type,"Line :", error_info.tb_lineno)
time.sleep(2)

soup=BeautifulSoup(page.text,"html.parser")

links=soup.find_all('a')
for link in links:
    #link=<a href=...........>Click me</a>
    count += 1
    #print(link.text)
    print(link.get('title'))
    #print(link['href'])

print("Total links " , count)