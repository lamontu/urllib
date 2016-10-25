import urllib.request
import re

req = urllib.request.urlopen('http://www.imooc.com/course/list?c=python')
buf = req.read()
rs = buf.decode()
listurl = re.findall(r'http://.+\.jpg', rs)
print(listurl)

i = 0
for url in listurl:
    f = open(str(i)+'.jpg', 'wb')
    req = urllib.request.urlopen(url)
    buf = req.read()
    # print(buf)
    f.write(buf)
    i += 1
