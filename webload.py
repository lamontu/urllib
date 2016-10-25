# -*- coding: utf8 -*-

from urllib import request
import http.cookiejar

url = 'http://www.baidu.com'


print('---------------------')
print('The First Method:')
response1 = request.urlopen(url)
print(response1.getcode())
print()
print(len(response1.read()))

print('---------------------')
print('The Second Method:')
req = request.Request(url)
req.add_header('user-agent', 'Mozilla/5.0')
response2 = request.urlopen(req)
print(response2.getcode())
print()
print(len(response2.read()))
print()

print('---------------------')
print('The Third Method:')
cj = http.cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cj))
request.install_opener(opener)
response3 = request.urlopen(url)
print(response3.getcode())
print()
print(cj)
print()
print(response3.read())
