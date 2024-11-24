import http.client
import json
import sys

def fetch_crypto_info(crypto_name):
    try :
        conn = http.client.HTTPSConnection('api.exchange.coinbase.com')
        payload = ''
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'python/https.client'
        }
        conn.request('GET', f'/currencies/{crypto_name}', payload, headers)
        resp = conn.getresponse()
        data = resp.read().decode('utf-8', errors='ignore')
        json_data = json.loads(data)
        print(json.dumps(json_data, indent=4))
    except ValueError as e:
        print(f'src/lib.py : fetch_crypto_info() :: ERROR ::: {e}')
        sys.exit(1)
    except Exception as e:
        print(f'src/lib.py.py : fetch_crypto_info() :: ERROR ::: {e}')
        sys.exit(1)
    finally:
        conn.close()

def fetch_crypto_price(crypto_name):
    try:
        conn = http.client.HTTPSConnection('api.exchange.coinbase.com')
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'python/https.client'
        }
        product_id = f'{crypto_name}-USD'
        conn.request('GET', f'/products/{product_id}/ticker', '', headers)
        resp = conn.getresponse()
        if resp.status != 200:
            raise Exception(f'src/lib.py : fetch_crypto_price() :: Failed to fetch data: HTTP {resp.status} {resp.reason}')
        data = resp.read().decode('utf-8', errors='ignore')
        json_data = json.loads(data)
        print(json.dumps(json_data, indent=4))
    except ValueError as e:
        raise ValueError(f'src/lib.py : fetch_crypto_price() :: ERROR ::: {e}')
    except Exception as e:
        raise Exception(f'src/lib.py : fetch_crypto_price() :: ERROR ::: {e}')
    finally:
        conn.close()