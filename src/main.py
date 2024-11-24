from util import check_user_input
from lib import *
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('src/main.py : __main__ :: ERROR ::: Must enter only one cryptocurrency name as a command line argument\n-> EXAMPLE USAGE (from root): python src/main.py BTC')
        sys.exit(1)
    crypto_name = check_user_input(sys.argv[1])
    fetch_crypto_info(crypto_name)
    fetch_crypto_price(crypto_name)
