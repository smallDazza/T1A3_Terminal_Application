

import unittest
from postal_zones import post_zone

class TestCubicWeight(unittest.TestCase):

    def test_1(self):
        # Test case for zone 0 & zone 5
        result = post_zone(0, 5)  
        self.assertEqual(result, 2.95)  # Expected result 

    def test_2(self):
        # Test case for zone 3 & zone 3
        result = post_zone(3, 3)
        self.assertEqual(result, 1.90)  # Expected result 

    def test_3(self):
        # Test case for zone 8 & zone 10
        result = post_zone(8, 10)  
        self.assertEqual(result, 6.95)  # Expected result 

    def test_4(self):
        # Test case for failing
        result = post_zone(10, 12)
        self.assertEqual(result, 3.05)  # Expected result to FAIL


if __name__ == '__main__':
    unittest.main()


