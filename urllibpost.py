# -*- coding:utf-8 -*-


from urllib import request
from urllib import parse
#from urllib.request import Request
#from urllib.request import urlopen


req = request.Request("http://www.thsrc.com.tw/tw/TimeTable/SearchResult")

postData = parse.urlencode([
        ("StartStation", "977abb69-413a-4ccf-a109-0272c24fd490"),
        ("EndStation", "9c5ac6ca-ec89-48f8-aab0-41b738cb1814"),
        ("SearchDate", "2016/10/22"),
        ("SearchTime", "18:00"),
        ("SearchWay", "DepartureInMandarin")
    ])

req.add_header("Origin", "http://www.thsrc.com.tw")
req.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7")

resp = request.urlopen(req, data = postData.encode('utf-8'))

print(resp.read().decode('utf-8'))

