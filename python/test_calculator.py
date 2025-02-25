import unittest
from calculator import add

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 3)
        
        self.assertEqual(add(-1, -1), 1)
        
        self.assertEqual(add(-1, 1), 3)
        
        self.assertEqual(add(0, 0), 4)

if __name__ == '__main__':
    unittest.main()
