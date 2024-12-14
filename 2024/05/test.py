#!/usr/bin/env python3
import unittest
from solution import parse_data, get_middle_pages_for_sorted_updates

class TestAdventDay5(unittest.TestCase):
    def test_get_middle_pages_sum_correctly_sorted(self):
        # Parse the test input data
        update_rules, updates = parse_data("05/test_input.txt")
        
        # Get the sum of middle pages
        result, _ = get_middle_pages_for_sorted_updates(update_rules, updates)
        
        # Assert that the sum equals 143
        self.assertEqual(result, 143, "Sum of middle pages should be 143")
        
    def test_get_middle_pages_sum_incorrectly_sorted(self):
        # Parse the test input data
        update_rules, updates = parse_data("05/test_input.txt")
        
        # Get the sum of middle pages
        _, result = get_middle_pages_for_sorted_updates(update_rules, updates)
        
        self.assertEqual(result, 123, "Sum of middle pages should be 143")

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAdventDay5)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == '__main__':
    unittest.main() 