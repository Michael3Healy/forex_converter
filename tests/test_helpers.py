from helpers import invalid_amount, invalid_code, invalid_inputs
from unittest import TestCase

class HelpersTestCase(TestCase):
    def test_invalid_inputs(self):
        self.assertEqual(invalid_inputs('asd', 'EUR', 50), 'Invalid Currency Code')
        self.assertEqual(invalid_inputs('USD', 'EUR', -10), 'Amount must be greater than 0')
        self.assertEqual(invalid_inputs('USD', 'EUR', 50), None)
    
    def test_invalid_code(self):
        self.assertEqual(invalid_code(['EUR', 'USD']), False)
        self.assertEqual(invalid_code(['EUR', 'asd']), True)

    def test_invalid_amount(self):
        self.assertEqual(invalid_amount(-10), True)
        self.assertEqual(invalid_amount(50), False)