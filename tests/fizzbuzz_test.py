from src.fizzbuzz import *

import unittest

class TestFizzbuzz(unittest.TestCase):

    def test_return_integer_1_as_string(self):
        return_integer_as_string = fizzbuzz(1)
        self.assertEqual( "1", return_integer_as_string)
    
    def test_return_integer_2_as_string(self):
        return_integer_as_string = fizzbuzz(2)
        self.assertEqual( "2", return_integer_as_string)

    def test_return_fizz_if_divisible_by_3(self):
        return_fizz_if_divisible_by_3 = fizzbuzz(3)
        self.assertEqual("Fizz", return_fizz_if_divisible_by_3)    

    def test_return_integer_4_as_string(self):
        return_integer_as_string = fizzbuzz(4)
        self.assertEqual("4", return_integer_as_string)
    
    def test_return_buzz_if_divisible_by_5(self):
        return_buzz_if_divisible_by_5 = fizzbuzz(5)
        self.assertEqual("Buzz", return_buzz_if_divisible_by_5)
    
    def test_if_not_divisible_by_3_and_5_return_integer_as_string(self):
        if_not_divisible_by_3_and_5_return_integer_as_string = fizzbuzz(7)
        self.assertEqual("7", if_not_divisible_by_3_and_5_return_integer_as_string)

    def test_return_fizzbuzzz_if_divisible_by_3_and_5(self):
        return_fizzbuzzz_if_divisible_by_3_and_5 = fizzbuzz(15)
        self.assertEqual("FizzBuzz", return_fizzbuzzz_if_divisible_by_3_and_5)


# test 1 : to take in the integer 1 and to return the integer as a string - "1"
# test 2 : to take in the integer 2 and to return the integer as a string - "2"
# test 3: to take in an integer and if divisible by 3 to return "Fizz" 
# test 4 : to take in the integer 4 and to return the integer as a string - "4"
# test 5: to take in an integer and if divisible by 5 to return "Buzz" 
# test 6: to take in an integer and if divisible by 3 & 5 to return "FizzBuzz" 
# test 7 : to take in an integer and if not divisible by 3 or 5 to return the integer as a string (as itself)