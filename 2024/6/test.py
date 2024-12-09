#!/usr/bin/env python3
import unittest
from solution import parse_data, move_guard, count_visited_cells, parse_data_as_matrix, find_guard_in_matrix

class TestAdventDay6(unittest.TestCase):
    def test_count_visited_cells(self):
        data = parse_data("6/test_input.txt")
        data_as_matrix, matrix_height, matrix_width = parse_data_as_matrix(data)
        guard_position = find_guard_in_matrix(data_as_matrix)
        move_guard(data_as_matrix, guard_position)
        result = count_visited_cells(data_as_matrix)
        self.assertEqual(result, 41, "Count of visited cells should be 41")

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAdventDay6)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == '__main__':
    unittest.main() 