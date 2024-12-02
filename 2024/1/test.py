import unittest
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

from solution import parse_data, puzzle_part_1, puzzle_part_2

class TestAdventDay1(unittest.TestCase):
    def setUp(self):
        self.data = parse_data("test_input.txt")
    
    def test_part1(self):
        result = puzzle_part_1(self.data)
        self.assertEqual(result, 11, "Part 1 should return 11")
    
    def test_part2(self):
        result = puzzle_part_2(self.data)
        self.assertEqual(result, 31, "Part 2 should return 31")

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAdventDay1)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == '__main__':
    main() 