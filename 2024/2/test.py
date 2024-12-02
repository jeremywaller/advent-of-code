import unittest
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

from solution import count_safe_lists, parse_data

class TestAdventDay2(unittest.TestCase):
    def setUp(self):
        self.data = parse_data("test_input.txt")
    
    def test_part1(self):
        result = count_safe_lists(self.data)
        self.assertEqual(result, 2, "Part 1 should return 2")
    
    def test_part2(self):
        result = count_safe_lists(self.data, 1)
        self.assertEqual(result, 4, "Part 2 should return 4")

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAdventDay2)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == '__main__':
    main() 