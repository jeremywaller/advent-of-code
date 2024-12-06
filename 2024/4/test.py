import unittest
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

from solution import search_grid_for_word, search_word_in_x_shape, parse_data, search_word

class TestAdventDay4(unittest.TestCase):
    def setUp(self):
        self.data = parse_data("test_input.txt")
    
    def test_search_grid_for_word(self):
        result = search_grid_for_word(self.data)
        expected = 18
        self.assertEqual(result, expected, "Should find 18 words")
    
    def test_search_word_in_x_shape(self):
        result = search_word_in_x_shape(self.data)
        expected = 9
        self.assertEqual(result, expected, "Should find 9 words in x shape")
        
def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAdventDay4)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == '__main__':
    main() 