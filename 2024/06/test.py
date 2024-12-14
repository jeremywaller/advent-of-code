#!/usr/bin/env python3
import unittest
from solution import parse_data, move_guard, count_visited_cells, parse_data_as_matrix, find_guard_in_matrix, count_successful_blockers

class TestAdventDay6(unittest.TestCase):
    def test_count_visited_cells(self):
        data = parse_data("06/test_input.txt")
        data_as_matrix, matrix_height, matrix_width = parse_data_as_matrix(data)
        guard_position = find_guard_in_matrix(data_as_matrix)
        move_guard(data_as_matrix, guard_position)
        result = count_visited_cells(data_as_matrix)
        self.assertEqual(result, 41, "Count of visited cells should be 41")
        
    def test_part2_successful_blockers(self):
        data = parse_data("06/test_input.txt")
        data_as_matrix, _, _ = parse_data_as_matrix(data)
        
        # Test Part 2
        successful_blockers = count_successful_blockers(data_as_matrix)
        self.assertEqual(successful_blockers, 6, "Expected 6 successful blockers")

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAdventDay6)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == '__main__':
    main() 