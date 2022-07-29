def fibonacci(num: int) -> int:
     # Write your code below
     if num>= 0 and num <= 2:
         return (num - 1)
     else:
         return (fibonacci(num-1) + fibonacci(num-2))


def fibonacci_without_recursion(n: int) -> int:
    if n>= 0 and n <= 2:
         return (n - 1)
    else:
         return (fibonacci(n-1) + fibonacci(n-2))


def reversed_number(num: int) -> int:

    """Given a number, write a function to output its reverse digits. 
    (e.g. given 123 the answer is 321) Make sure that if it is a negative 
    number you keep the negative in the front (-123 becomes -321)
    """
    reversed_num = 0
    
    while n != 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    return reversed_num
        

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
        self.assertEqual(fibonacci(35), 5702887)
        LOGGER.info("Fibonacci passed the test successfully")



if __name__ == '__main__':
    print()
    print('=' * 50)
    print("Test Results for Lesson3's Assessments")
    print('=' * 50)
    unittest.main()
