import http.client
import json

if __name__ == '__main__':
    conn = http.client.HTTPSConnection('api.exchange.coinbase.com')
    payload = ''
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'python'
    }
    conn.request('GET', '/currencies/DOGE', payload, headers)
    resp = conn.getresponse()
    data = resp.read()
    print(data.decode('utf-8'))
