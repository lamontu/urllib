# -*- coding: utf-8 -*-

from urllib import request
from urllib import parse

URL_IP = 'http://127.0.0.1:8000/ip'
URL_GET = 'http://127.0.0.1:8000/get'

def use_simple_urllib():
    response = request.urlopen(URL_IP)
    print('>>>>Response Headers:')
    print(response.info())
    
    print('>>>>Response Body:')
    print(''.join([line.decode('utf-8') for line in response.readlines()]))

def use_params_urllib():
    params = parse.urlencode({'para1':'hello', 'para2':'world'})
    print('Request Params:')
    print(params)
    response = request.urlopen('?'.join([URL_GET, '%s']) % params)

    print('>>>>Response Headers:')
    print(response.info())
    print('>>>>Status Code:')
    print(response.getcode())    
    print('>>>>Response Body:')
    print(''.join([line.decode('utf-8') for line in response.readlines()]))

if __name__ == '__main__':
    print('>>>Use simple urllib:')
    use_simple_urllib()
    print('>>>Use params urllib:')
    use_params_urllib()
