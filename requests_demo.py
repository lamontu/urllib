# -*- coding: utf-8 -*-

import requests

URL_IP = 'http://127.0.0.1:8000/ip'
URL_GET = 'http://127.0.0.1:8000/get'

def use_simple_requests():
    response = requests.get(URL_IP)

    print('>>>>Response Headers:')
    print(response.headers)
    
    print('>>>>Status Code:')
    print(response.status_code)
    print(response.reason)

    print('>>>>Response Body:')
    print(response.text)

def use_params_requests():
    paramDict = {'para1':'hello', 'para2':'world'}
    response = requests.get(URL_GET, params = paramDict)
    print('Request Params:')
    print(paramDict)

    print('>>>>Response Headers:')
    print(response.headers)

    print('>>>>Status Code:')
    print(response.status_code)
    print(response.reason)

    print('>>>>Response Body:')
    print(response.json())

if __name__ == '__main__':
    print('>>>Use simple requests:')
    use_simple_requests()

    print('>>>Use params requests:')
    use_params_requests()

