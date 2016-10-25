# -*- coding:utf-8 -*-

from urllib import request


req = request.Request("http://www.baidu.com")
req.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7")

resp = request.urlopen(req)

print(resp.read().decode('utf-8'))

