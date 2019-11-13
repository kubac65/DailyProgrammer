import unittest
from . import taxlib

test_data = [
    (0, 0),
    (10000, 0),
    (10009, 0),
    (10010, 1),
    (12000, 200),
    (56789, 8697),
    (1234567, 473326)
]

class TaxTests(unittest.TestCase):
    def test_validate_calculations(self):
        for input_data, expected_output in test_data:
            with self.subTest():
                result = taxlib.tax(input_data)
                self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()