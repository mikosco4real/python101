def fibonacci(num: int) -> int:
     # Write your code below
     if num> 0 and num <= 2:
         return (num - 1)
     else:
         return (fibonacci(num-1) + fibonacci(num-2))


def fibonacci_without_recursion(n: int) -> int:
    last_number = 0
    last_two_numbers = 0
    iteration = 1
    fib = 0

    while iteration < n:
        iteration += 1
        if iteration == 1:
            continue
        if iteration == 2:
            fib = 1
            last_number = 1
            continue

        fib = last_number + last_two_numbers
        last_two_numbers = last_number
        last_number = fib

    return fib


def reversed_number(num: int) -> int:

    """Given a number, write a function to output its reverse digits. 
    (e.g. given 123 the answer is 321) Make sure that if it is a negative 
    number you keep the negative in the front (-123 becomes -321)
    """

    reversed_num = 0
    negative = False
    
    if num < 0:
        negative = True
        num = num * (-1)
    
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    
    if negative:
        return reversed_num * (-1)
    return reversed_num

def reversed_number_2(num: int) -> int:
    num = str(num)
    if num.startswith('-'):
        num = num[1:]
        return int("-" + "".join(reversed(num)))

    return int(num[::-1])
        

print(fibonacci_without_recursion(9))

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