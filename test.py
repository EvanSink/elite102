import unittest
from num_operations import is_odd
from num_operations import is_even

class TestNumbersOperations(unittest.TestCase):
    def test_is_odd(self):
        self.assertEqual(is_odd(3), True)
        self.assertEqual(is_odd(4), False)
        self.assertEqual(is_odd(0), False)
        self.assertEqual(is_odd(-1), True)
    def test_is_even(self):
        self.assertEqual(is_even(3), False)
        self.assertEqual(is_even(4), True)
        self.assertEqual(is_even(0), True)
        self.assertEqual(is_even(-1), False)

if __name__ == "__main__":
    unittest.main()