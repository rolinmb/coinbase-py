from util import check_user_input
import http.client
import json
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('src/main.py : __main__ :: ERROR ::: Must enter only one cryptocurrency name as a command line argument\n-> EXAMPLE USAGE (from root): python src/main.py BTC')
        sys.exit(1)
    try :
        crypto_name = check_user_input(sys.argv[1])
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
        print(f'src/main.py : __main__ :: ERROR ::: {e}')
        sys.exit(1)
    except Exception as e:
        print(f'src/main.py : __main__ :: ERROR ::: {e}')
        sys.exit(1)
