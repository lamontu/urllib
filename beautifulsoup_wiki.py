# -*- coding:utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#resp = urlopen("http://en.wikipedia.org/wiki/Main_Page").read().decode("utf-8")
resp = urlopen("http://en.wikipedia.org/wiki/Main_Page").read() #Same as above 
soup = BeautifulSoup(resp, "html.parser")
print(soup.original_encoding)
listUrls = soup.find_all("a", href = re.compile("^/wiki/"))

print(type(listUrls))    # <clsss 'bs4.element.ResultSet'>
urls = [url for url in listUrls]
print(type(urls))    # <class 'list'>
print(type(urls[0])) # <class 'bs4.element.Tag'>

for url in listUrls:
    if not re.search("\.(jpg|JPG|png|PNG)$", url["href"]): 
        #print(url.get_text(), "<---->", url["href"]) # Same sa below
        print(url.string, "<---->", "http://en.wikipedia.org" +  url["href"])


#print(soup)

#print(resp)
