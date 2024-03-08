from flask import Flask, request, render_template,  session, jsonify, redirect, flash
import requests
from pdb import set_trace
from helpers import get_symbol, invalid_code, invalid_inputs

app = Flask(__name__)

app.config['SECRET_KEY'] = 'aksjhdcajk'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

API_KEY = 'fca_live_VnO8Q6X7GwJYqaEM7jRYKLGuwTjxTUe8Nls1RyUt'
BASE_URL = 'https://api.freecurrencyapi.com/v1/'

@app.route('/')
def get_converter():
    return render_template('index.html')

@app.route('/currency_symbol', methods=['POST'])
def get_currency_symbols():
    '''Adds info from form to session object, retrieves currency symbols, and redirects back to /convert where results are displayed'''

    base_curr = session['base_curr'] = request.form.get('base')
    new_curr = session['new_curr'] = request.form.get('new')
    amount = session['amount'] = float(request.form.get('amount'))
    headers = {'apikey': API_KEY}

    if not invalid_inputs(base_curr, new_curr, amount):
        currency_list = requests.get(f'{BASE_URL}/currencies', headers=headers, params={'currencies': f"{session['base_curr']},{session['new_curr']}"})
        session['base_symbol'] = get_symbol(currency_list, session['base_curr'])
        session['new_symbol'] = get_symbol(currency_list, session['new_curr'])
        return redirect('/convert')
    else:
        flash(invalid_inputs(base_curr, new_curr, amount), 'error')
        return redirect('/')
    

@app.route('/convert')
def get_conversion():
    '''Gets conversion results from API and sends them to html template'''

    # Retrieve values to use in request and send to template
    base_curr = session['base_curr']
    base_symbol = session['base_symbol']
    new_curr = session['new_curr']
    new_symbol = session['new_symbol']
    amount = session['amount']

    # apikey set as header for security reasons
    headers = {'apikey': API_KEY}
    
    response = requests.get(f'{BASE_URL}/latest', headers=headers, params={'base_currency': base_curr, 'currencies': new_curr}, allow_redirects=False)
    results = response.json().get('data')
    new_value = round(float(results[new_curr]) * amount, 2)

    return render_template('index.html', base_curr=base_curr, base_symbol=base_symbol, new_curr=new_curr, new_symbol=new_symbol, amount=amount, new_value=new_value)





