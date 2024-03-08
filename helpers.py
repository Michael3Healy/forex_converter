import requests
from pdb import set_trace

def get_symbol(response, curr):
    '''Gets currency symbol of currency (ex. $)'''
    return response.json()['data'][curr]['symbol_native']

def invalid_inputs(base_curr, new_curr, amount):
    '''Runs through all functions to check inputs and returns corresponding error message to be flashed'''

    if invalid_code([base_curr, new_curr]):
        return 'Invalid Currency Code'
    
    if invalid_amount(amount):
        return 'Amount must be greater than 0' 
    
    return None

def invalid_code(currencies):
    '''Iterates through list of currencies and checks that they all exist in API's currency list'''

    data = requests.get('https://api.freecurrencyapi.com/v1/currencies', headers={'apikey': 'fca_live_VnO8Q6X7GwJYqaEM7jRYKLGuwTjxTUe8Nls1RyUt'})
    valid_currencies = data.json()['data'].keys()

    for currency in currencies:
        if currency not in valid_currencies:
            return True
    return False

def invalid_amount(amount):
    return amount <= 0
    

    