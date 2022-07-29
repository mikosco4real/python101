def fibonacci(num: int) -> int:
    # Write your code below
    pass

def fibonacci_without_recursion(num: int) -> int:
    pass

def reversed_number(num: int) -> int:
    """Given a number, write a function to output its reverse digits. 
    (e.g. given 123 the answer is 321) Make sure that if it is a negative 
    number you keep the negative in the front (-123 becomes -321)
    """
    pass

# Examiners Section

import unittest
import logging

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

class TestAssessmentResults(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(fibonacci(1), 0)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 1)
        self.assertEqual(fibonacci(4), 2)
        self.assertEqual(fibonacci(20), 4181)
        self.assertEqual(fibonacci(35), 9227465)
        LOGGER.info("Fibonacci passed the test successfully")
    
    def test_reversed_number(self):
        self.assertEqual(reversed_number(234), 432)
        self.assertEqual(reversed_number(123), 321)
        self.assertEqual(reversed_number(-3247832), -2387423)
        self.assertEqual(reversed_number(123456789), 987654321)
        self.assertEqual(reversed_number(23324958), 85942332)
        LOGGER.info("Reversed Number passed the test successfully")



if __name__ == '__main__':
    print()
    print('=' * 50)
    print("Test Results for Lesson3's Assessments")
    print('=' * 50)
    unittest.main()