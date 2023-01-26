import requests
from bs4 import BeautifulSoup

URL = 'https://www.vg.no/'
page = requests.get(URL)

soup = BeautifulSoup(page.content,"html.parser")

results = soup.find(class_="articles")
#print(results)
#titler = results.find_all("div", class_="articles")
titler = results.find_all("h3")
#print(titler)
for title in titler:
    print(title.text)#.strip()) 
#print(results.prettify())