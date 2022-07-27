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



if __name__ == '__main__':
    print()
    print('=' * 50)
    print("Test Results for Lesson3's Assessments")
    print('=' * 50)
    unittest.main()