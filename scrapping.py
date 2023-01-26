import requests
from bs4 import BeautifulSoup

URL = 'https://www.vg.no/'
page = requests.get(URL)

soup = BeautifulSoup(page.content,"html.parser")

results = soup.find(class_="app")
#print(results)
#titler = results.find_all("div", class_="articles")
titler = results.find_all("h3", class_="headline")
#print(titler)
for title in titler:
    kul = title.text
    lower = kul.lower()
    #print(lower)
    if "jeg" in lower:
        print("1")
    #if "Jeg" in title.text:
    #   print("1")
    #print(title.text)#.strip()) 

#print(results.prettify())

#antall_ganger_nevnt = results.find_all("h3", string= lambda text: "jonas" in text.lower())

#print(len(antall_ganger_nevnt))




def sjekk_poeng(politiker):
    poeng = 0
    URL = 'https://www.vg.no/'
    page = requests.get(URL)


    soup = BeautifulSoup(page.content,"html.parser")

    results = soup.find(class_="app")
    #print(results)
    #titler = results.find_all("div", class_="articles")
    titler = results.find_all("h3", class_="headline")
    #print(titler)
    for title in titler:
        kul = title.text
        lower = kul.lower()
        #print(lower)
        if str(politiker).lower() in lower:
            poeng += 1

    return poeng

