# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup as bs
import re

html_doc = """
<html><head><title>The Dormouse's story<a>Hello</a></title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://exampleScomtillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = bs(html_doc, "html.parser")

print(soup.prettify())

print(soup.title)
print(soup.title.string)
print(soup.title.get_text())
print(soup.a)

print()
print(soup.find(id="link2").string)
print(soup.find_all("a"))
print([strlink.string for strlink in soup.findAll("a")])

print()
print(soup.find("p", {"class":"story"}))
print(soup.find("p", {"class":"story"}).get_text())

print()
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)

print()
data = soup.find_all("a", href = re.compile(r"^http://example.com/"))
print(data)
