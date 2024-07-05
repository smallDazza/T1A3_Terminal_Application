

import unittest
from timepackage.delivery_times import del_time

class TestCubicWeight(unittest.TestCase):

    def test_1(self):
        # Test case for zone 0 to zone 4
        result = del_time(0, 4)  
        self.assertEqual(result, "2-3")  # Expected result 

    def test_2(self):
        # Test case for zone 5 to zone 5
        result = del_time(5, 5)
        self.assertEqual(result, "3-4")  # Expected result 

    def test_3(self):
        # Test case for zone 2 to zone 10
        result = del_time(2, 10)  
        self.assertEqual(result, "4-6(Darwin)4-14(Other Areas)")  # Expected result 

    def test_4(self):
        # Test case for failing zone 0 to zone 3
        result = del_time(0, 3)
        self.assertEqual(result, "2-3")  # Expected result to FAIL


if __name__ == '__main__':
    unittest.main()


