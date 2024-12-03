import unittest
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

from solution import get_result, find_mul_instructions, perform_mul_instructions, parse_data

class TestAdventDay3(unittest.TestCase):
    def setUp(self):
        self.data = parse_data("test_input.txt")
    
    def test_get_result(self):
        result = get_result(self.data)
        expected = 161
        self.assertEqual(result, expected, "Should process the full string correctly")
    
    def test_get_result_with_test_input_and_dont(self):
        result = get_result(self.data, enforce_do_instructions=True)
        expected = 48 
        self.assertEqual(result, expected, "Should process test input correctly with don't() blocks")

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAdventDay3)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == '__main__':
    main() 