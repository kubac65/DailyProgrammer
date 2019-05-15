import unittest
from . import fitlib

# Test data contains list of tuples representing following information
# (cx, cy, bx, by, expected result)
fit1_test_data = [
    (25, 18, 6, 5, 12),
    (10, 10, 1, 1, 100),
    (12, 34, 5, 6, 10),
    (12345, 678910, 1112, 1314, 5676),
    (5, 100, 6, 1, 0)
]

fit2_test_data = [
    (12, 34, 5, 6, 12),
    (25, 18, 6, 5, 15),
    (12345, 678910, 1112, 1314, 5676),
    (5, 5, 3, 2, 2),
    (5, 100, 6, 1, 80),
    (5, 5, 6, 1, 0)
]

fit3_test_data = [
    (10, 10, 10, 1, 1, 1, 1000),
    (12, 34, 56, 7, 8, 9, 32),
    (123, 456, 789, 10, 11, 12, 32604),
    (1234567, 89101112, 13141516, 171819, 202122, 232425, 174648)
]

fitn_test_data = [
    ([3, 4], [1, 2], 6),
    ([123, 456, 789], [10, 11, 12], 32604),
    ([123, 456, 789, 1011, 1213, 1415], [16, 17, 18, 19, 20, 21], 1883443968),
    # ultimate test, so far crashing with my O(N!) implementation
    #([180598, 125683, 146932, 158296, 171997, 204683, 193694, 216231, 177673, 169317, 216456, 220003, 165939, 205613, 152779, 177216, 128838, 126894, 210076, 148407], [1984, 2122, 1760, 2059, 1278, 2017, 1443, 2223, 2169, 1502, 1274, 1740, 1740, 1768, 1295, 1916, 2249, 2036, 1886, 2010], 4281855455197643306306491981973422080000
]

class FitLibTests(unittest.TestCase):
    def test_fit1(self):
        self.excercise_function(fitlib.fit1, fit1_test_data)

    def test_fit2(self):
        self.excercise_function(fitlib.fit2, fit2_test_data)

    def test_fit3(self):
        for cx, cy, cz, bx, by, bz, expected_result in fit3_test_data:
            with self.subTest():
                actual_result = fitlib.fit3(cx, cy, cz, bx, by, bz)
                self.assertEqual(actual_result, expected_result, "Actual result does not match expected result")

    def test_fitn(self):
        for c, b, expected_result in fitn_test_data:
            with self.subTest():
                actual_result = fitlib.fitn(c, b)
                self.assertEqual(actual_result, expected_result, "Actual result does not match expected result")

    def excercise_function(self, function, data_set):
        for cx, cy, bx, by, expected_result in data_set:
            with self.subTest():
                actual_result = function(cx, cy, bx, by)
                self.assertEqual(actual_result, expected_result, "Actual result does not match expected result")

if __name__ == '__main__':
    unittest.main()