def check_user_input(crypto_name):
    if len(crypto_name) < 2:
        raise ValueError('check_user_input() :: ERROR ::: Cryptocurrency name must be at least 3 alphabetical characters.')
    if len(crypto_name) > 6:
        raise ValueError('check_user_input() :: ERROR ::: Cryptocurrency name must be at most 5 alphabetical characters.')
    if not crypto_name.isalpha():
        raise ValueError('check_user_input() :: ERROR ::: Cryptocurrency name must only contain alphabetical characters.')
    return crypto_name.upper()
