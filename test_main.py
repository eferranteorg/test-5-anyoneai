import unittest
from main import return_five

class TestReturnFive(unittest.TestCase):
    def test_return_five(self):
        self.assertEqual(return_five(), 5)

if __name__ == '__main__':
    unittest.main()
