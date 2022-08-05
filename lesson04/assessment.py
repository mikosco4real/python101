def format_number(num: int) -> str:
    """Write a function named 'format_number' that takes a non-negative number as its only parameter. 
    Your function should convert the number to a string and add commas as a thousand separators. 
    For example, calling format_number(1000000) should return "1,000,000"
    """
    new_num = 1000   
    if num < new_num:
        return str(num)
    return str('{:,}'.format(num))
    
             
    

# Examiners Section

import unittest
import logging

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

class TestAssessmentResults(unittest.TestCase):

    def test_format_number(self):
        self.assertEqual(format_number(1000), '1,000')
        self.assertEqual(format_number(32432546), '32,432,546')
        self.assertEqual(format_number(1000000), '1,000,000')
        self.assertEqual(format_number(50000), '50,000')
        self.assertEqual(format_number(356231000), '356,231,000')
        self.assertEqual(format_number(47236400), '47,236,400')
        self.assertEqual(format_number(900), '900')
        LOGGER.info("Fibonacci passed the test successfully")



if __name__ == '__main__':
    print()
    print('=' * 50)
    print("Test Results for Lesson3's Assessments")
    print('=' * 50)
    unittest.main()