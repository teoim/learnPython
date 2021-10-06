#
# WEB SCRAPPING with the BeautifulSoup library
#
# In cmd:
#   "pip install requests"
#   "pip install BeautifulSoup4"
#
# Useful BeautifulSoup methods:
#   find('a')   # finds anchors
#   find_all("a")   # finds all anchors
#   find_parent("a")    # find parent of anchors
#   find_next_siblings("a")
#

import requests
from bs4 import BeautifulSoup

# AccuWeather Bucharest hourly weather
#response1 = requests.get("https://www.accuweather.com/en/ro/bucharest/287430/hourly-weather-forecast/287430")
#print(response1.content)   # <Response [403>]  (Access Denied)

#response2 = requests.get("https://fmi.unibuc.ro/")
response2 = requests.get("https://www.imobiliare.ro/inchirieri-apartamente/bucuresti-ilfov?id=82493648")
print(response2)    # <Response [200]>
print(response2.status_code)    # 200
# print(response2.content)  # Full html page

# When response_code is 200, you can parse the content using the BeautifulSoup library :

soup = BeautifulSoup(response2.content, "html.parser")   # pass the content and the type of parser
#print(soup)
#print(soup.prettify())  # Adds indentation


#   find('a')   # finds anchors
#   find_all("a")   # finds all anchors
#   find_parent("a")    # find parent of anchors
#   find_next_siblings("a")

card = soup.find( "div", attrs={"class":"box-anunt"})
#print(card.prettify())

price = card.find( "span", attrs={"class":"pret-mare"})
#print(price.text)

currencyVat = card.find( "span", attrs={"class":"tva-luna"})
#print(currencyVat.text)

location = card.find( "div", attrs={"class":"localizare"})
#print(location.find("p").text.strip("\t\n ")) # get rid of tabs, new lines and white spaces
metroDist = location.find("div").text.strip("\t\n ")
location = location.find("p").text.strip("\t\n ")

data = "Zona: {} la pretul de {} {}. Distanta metrou: {}".format( location ,  price.text , currencyVat.text, metroDist)
print(data)




# DO THE SAME AS ABOVE FOR ALL CARDS ON THE PAGE ( only first page)
# TODO: do the same for all pages (available at the bottom of the first page you have the number of pages)
print( "==================================ALL CARDS ON FIRST PAGE========================================" )
cards = soup.find_all( "div", attrs={"class":"box-anunt"}, id=True)
#print(cards.prettify())
count = 0
for card in cards:
    price = card.find( "span", attrs={"class":"pret-mare"})
    #print(price.text)

    currencyVat = card.find( "span", attrs={"class":"tva-luna"})
    #print(currencyVat.text)

    location = card.find( "div", attrs={"class":"localizare"})
    #print(location.find("p").text.strip("\t\n ")) # get rid of tabs, new lines and white spaces
    #metroDist = location.find("div").text.strip("\t\n ")
    location = location.find("p").text.strip("\t\n ")

    details = card.find( "ul", attrs={"class":"caracteristici"})
    details = details.find_all("span")
    detailsText = "| "
    for span in details:
        detailsText = detailsText + span.text + " | "
    #print(detailsText)

    data = "| Location: {} ; Price: {} {}.".format( location ,  price.text , currencyVat.text)
    count+=1
    print(count)
    print(data)
    print(detailsText)

exit()  # comment this if you want to scrape the whole thing

# get total number of pages
pagesDiv = soup.find("div",attrs={"class":"index_paginare"})
#print(pagesDiv)
pagini = pagesDiv.find_all("a",attrs={"class":"butonpaginare"})
#print(pagini[-2].text)
nrPagini = pagini[-2].text


# do the same for all pages (available at the bottom of the first page you have the number of pages)
print( "===============================ALL CARDS ON ALL PAGES=========================================" )

count = 0   # Number of records
for i in range(int(nrPagini)):
    #print(i+1)
    link = "https://www.imobiliare.ro/inchirieri-apartamente/bucuresti-ilfov?id=82493648&pagina=" + str(i+1)
    print(link)

    # INCARCA PAGINA
    response3 = requests.get(link)
    #print(response2)    # <Response [200]>
    #print(response2.status_code)    # 200
    # print(response2.content)  # Full html page

    # When response_code is 200, you can parse the content using the BeautifulSoup library :

    soup = BeautifulSoup(response3.content, "html.parser")

    cards = soup.find_all( "div", attrs={"class":"box-anunt"}, id=True)
    #print(cards.prettify())
    file = open( "APARTMENT_DATA.txt", "a")
    file.write( link + "\n")
    for card in cards:
        price = card.find( "span", attrs={"class":"pret-mare"})
        #print(price.text)
        if price == None:
            price = "???"
        else:
            price=price.text

        currencyVat = card.find( "span", attrs={"class":"tva-luna"})
        #print(currencyVat.text)
        if currencyVat == None:
            currencyVat = "???"
        else:
            currencyVat=currencyVat.text


        location = card.find( "div", attrs={"class":"localizare"})
        #print(location.find("p").text.strip("\t\n ")) # get rid of tabs, new lines and white spaces
        #metroDist = location.find("div").text.strip("\t\n ")
        location = location.find("p").text.strip("\t\n ")

        data = "Zona: {} la pretul de {} {}.\n".format( location ,  price , currencyVat)
        count+=1
        #print(count, " - ", data)
        #print(data)
        file.write( str(count) + " - " + data)
    file.close()
#end
