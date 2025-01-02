from util import *
import http.client
import json
import sys

def fetch_crypto_info():
    if len(sys.argv) != 2:
        print('src/lib.py : fetch_crypto_info() :: ERROR ::: Must enter only one cryptocurrency name as a command line argument\n-> EXAMPLE USAGE (from root): python src/main.py BTC')
        sys.exit(1)
    crypto_name = check_user_input(sys.argv[1])
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
        print('src/lib.py : fetch_crypto_info() :: '+crypto_name+' Info :::\n'+json.dumps(json_data, indent=4))
    except ValueError as e:
        print(f'src/lib.py : fetch_crypto_info() :: ERROR ::: {e}')
        sys.exit(1)
    except Exception as e:
        print(f'src/lib.py.py : fetch_crypto_info() :: ERROR ::: {e}')
        sys.exit(1)
    finally:
        conn.close()

def fetch_crypto_quote():
    if len(sys.argv) != 2:
        print('src/lib.py : fetch_crypto_price() :: ERROR ::: Must enter only one cryptocurrency name as a command line argument\n-> EXAMPLE USAGE (from root): python src/main.py BTC')
        sys.exit(1)
    crypto_name = check_user_input(sys.argv[1])
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
        print('src/lib.py : fetch_crypto_quote() :: '+crypto_name+' Quote :::\n'+json.dumps(json_data, indent=4))
    except ValueError as e:
        raise ValueError(f'src/lib.py : fetch_crypto_price() :: ERROR ::: {e}')
    except Exception as e:
        raise Exception(f'src/lib.py : fetch_crypto_price() :: ERROR ::: {e}')
    finally:
        conn.close()

def fetch_ratio_quote():
    if len(sys.argv) != 3:
        print('src/lib.py : fetch_ratio_quote() :: ERROR ::: Must enter two cryptocurrency names as command line arguments for ratio quote\n-> EXAMPLE USAGE (from root): python src/main.py ETH BTC')
        sys.exit(1)
    cname0 = check_user_input(sys.argv[1])
    cname1 = check_user_input(sys.argv[2])
    cprice0 = 0.0
    cprice1 = 0.0
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'python/https.client'
    }
    try:
        conn = http.client.HTTPSConnection(APIURL)
        product_id = f'{cname0}-USD'
        conn.request('GET', f'/products/{product_id}/ticker', '', headers)
        resp = conn.getresponse()
        if resp.status != 200:
            raise Exception(f'src/lib.py : fetch_ratio_quote() :: Failed to fetch data: HTTP {resp.status} {resp.reason}')
        data = resp.read().decode('utf-8', errors='ignore')
        json_data = json.loads(data)
        cprice0 = float(json_data['price'])
    except ValueError as e:
        raise ValueError(f'src/lib.py : fetch_ratio_quote() :: ERROR ::: {e}')
    except Exception as e:
        raise Exception(f'src/lib.py : fetch_ratio_quote() :: ERROR ::: {e}')
    finally:
        try:
            product_id = f'{cname1}-USD'
            conn.request('GET', f'/products/{product_id}/ticker', '', headers)
            resp = conn.getresponse()
            if resp.status != 200:
                raise Exception(f'src/lib.py : fetch_ratio_quote() :: Failed to fetch data: HTTP {resp.status} {resp.reason}')
            data = resp.read().decode('utf-8', errors='ignore')
            json_data = json.loads(data)
            cprice1 = float(json_data['price'])
        except ValueError as e:
            raise ValueError(f'src/lib.py : fetch_ratio_quote() :: ERROR ::: {e}')
        except Exception as e:
            raise Exception(f'src/lib.py : fetch_ratio_quote() :: ERROR ::: {e}')
        finally:
            ratio = cprice0/cprice1
            print(f'\nsrc/lib.py : fetch_ratio_quote() :: {cname0}/{cname1} = {ratio}')
            conn.close()

