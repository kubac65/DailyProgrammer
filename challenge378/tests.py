import unittest
from . import detectivelib

warmup1_test_data = [
    ([5, 3, 0, 2, 6, 2, 0, 7, 2, 5], [5, 3, 2, 6, 2, 7, 2, 5]),
    ([5, 3, 0, 2, 6, 2, 0, 7, 2, 5], [5, 3, 2, 6, 2, 7, 2, 5]),
    ([5, 3, 0, 2, 6, 2, 0, 7, 2, 5], [5, 3, 2, 6, 2, 7, 2, 5]),
    ([4, 0, 0, 1, 3], [4, 1, 3]),
    ([1, 2, 3], [1, 2, 3]),
    ([0, 0, 0], []),
    ([], [])
]

warmup2_test_data = [
    ([5, 1, 3, 4, 2], [5, 4, 3, 2, 1]),
    ([0, 0, 0, 4, 0], [4, 0, 0, 0, 0]),
    ([1], [1]),
    ([], [])
]

warmup3_test_data = [
    (7, [6, 5, 5, 3, 2, 2, 2], False),
    (5, [5, 5, 5, 5, 5], False),
    (5, [5, 5, 5, 5], True),
    (3, [1, 1], True),
    (1, [],True),
    (0, [], False)
]

warmup4_test_data = [
    (4, [5, 4, 3, 2, 1], [4, 3, 2, 1, 1]),
    (11, [14, 13, 13, 13, 12, 10, 8, 8, 7, 7, 6, 6, 4, 4, 2], [13, 12, 12, 12, 11, 9, 7, 7, 6, 6, 5, 6, 4, 4, 2]),
    (1, [10, 10, 10], [9, 10, 10]),
    (3, [10, 10, 10], [9, 9, 9]),
    (1, [1], [0])
]

hh_test_data = [
    ([5, 3, 0, 2, 6, 2, 0, 7, 2, 5], False),
    ([4, 2, 0, 1, 5, 0], False),
    ([3, 1, 2, 3, 1, 0], True),
    ([16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16], True),
    ([14, 10, 17, 13, 4, 8, 6, 7, 13, 13, 17, 18, 8, 17, 2, 14, 6, 4, 7, 12], True),
    ([15, 18, 6, 13, 12, 4, 4, 14, 1, 6, 18, 2, 6, 16, 0, 9, 10, 7, 12, 3], False),
    ([6, 0, 10, 10, 10, 5, 8, 3, 0, 14, 16, 2, 13, 1, 2, 13, 6, 15, 5, 1], False),
    ([2, 2, 0], False),
    ([3, 2, 1], False),
    ([1, 1], True),
    ([1], False),
    ([], True)
]

class DetectiveTests(unittest.TestCase):
    def test_warmup1(self):
        self._warmup_executor(warmup1_test_data, detectivelib.warmup1)

    def test_warmup2(self):
        self._warmup_executor(warmup2_test_data, detectivelib.warmup2)

    def test_warmup3(self):
        for n, seq, expected_output in warmup3_test_data:
            with self.subTest():
                actual_output = detectivelib.warmup3(n, seq)
                self.assertEqual(actual_output, expected_output)

    def test_warmup4(self):
        for n, seq, expected_output in warmup4_test_data:
            with self.subTest():
                actual_output = detectivelib.warmup4(n, seq)
                self.assertSequenceEqual(actual_output, expected_output)

    def test_hh(self):
        for seq, expected_output in hh_test_data:
            with self.subTest():
                actual_output = detectivelib.hh(seq)
                self.assertEqual(actual_output, expected_output)

    def _warmup_executor(self, test_data, function):
        for input_data, expected_output in test_data:
            with self.subTest():
                actual_output = function(input_data)
                self.assertSequenceEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()