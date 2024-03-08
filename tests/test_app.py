from app import get_converter, get_currency_symbols, get_conversion, app
from unittest import TestCase

app.config['TESTING'] = True

class AppTestCase(TestCase):
    def test_home_page(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<form action="/currency_symbol"', html)

    def test_currency_form_post(self):
        with app.test_client() as client:
            valid_req_resp = client.post('/currency_symbol', data={'base': 'USD', 'new': 'USD', 'amount': '1'})
            invalid_req_resp = client.post('/currency_symbol', data={'base': 'asd', 'new': 'fgh', 'amount': '-10'})

            self.assertEqual(valid_req_resp.status_code, 302)
            self.assertEqual(valid_req_resp.location, 'http://localhost/convert')

            self.assertEqual(invalid_req_resp.status_code, 302)
            self.assertEqual(invalid_req_resp.location, 'http://localhost/')

    def test_conversion(self):
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['base_curr'] = 'USD'
                sess['base_symbol'] = '$'
                sess['new_curr'] = 'USD'
                sess['new_symbol'] = '$'
                sess['amount'] = 1.0

            resp = client.get('/convert')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('$1.00 is worth $1.0', html)