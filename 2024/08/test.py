#!/usr/bin/env python3
import unittest
from solution import parse_data, calculate_distance, calculate_antinodes_distances, place_antinodes, get_coordinates_of_antennas, count_antinodes_withing_grid

class TestAdventDay8(unittest.TestCase):
    def setUp(self):
        self.test_grid = [
            [".", "1", "."],
            ["1", ".", "."],
            [".", ".", "."]
        ]
        
    def test_parse_data(self):
        grid = parse_data("8/test_input.txt")
        self.assertIsInstance(grid, list)
        self.assertIsInstance(grid[0], list)
        
    def test_calculate_distance(self):
        antenna1 = (0, 1)
        antenna2 = (1, 0)
        expected_distance = (-1, 1)
        self.assertEqual(calculate_distance(antenna1, antenna2), expected_distance)
        
    def test_get_coordinates_of_antennas(self):
        antennas = get_coordinates_of_antennas(self.test_grid)
        expected = {"1": [(0, 1), (1, 0)]}
        self.assertEqual(antennas, expected)
        
    def test_calculate_antinodes_distances(self):
        antennas = {"1": [(0, 1), (1, 0)]}
        antinodes = calculate_antinodes_distances(antennas)
        self.assertEqual(len(antinodes), 1)
        self.assertEqual(len(antinodes[0]), 4)
        
    def test_place_antinodes(self):
        antinodes = [("1", (0, 1), (1, 0), (-1, 1))]    
        max_range = (3, 3)
        locations = place_antinodes(antinodes, max_range, include_resonance=False)
        self.assertIsInstance(locations, set)
        self.assertEqual(len(locations), 2)
        
    def test_count_antinodes_full_workflow(self):
        grid = parse_data("8/test_input.txt")
        max_range = (len(grid), len(grid[0]))
        antennas = get_coordinates_of_antennas(grid)
        antinode_locations = calculate_antinodes_distances(antennas)
        locations = place_antinodes(antinode_locations, max_range, include_resonance=False)
        count = count_antinodes_withing_grid(grid, locations)
        self.assertEqual(count, 14, "Expected 14 antinodes within the grid")
        
    def test_count_antinodes_with_resonance(self):
        grid = parse_data("8/test_input.txt")
        max_range = (len(grid), len(grid[0]))
        antennas = get_coordinates_of_antennas(grid)
        antinode_locations = calculate_antinodes_distances(antennas)
        locations = place_antinodes(antinode_locations, max_range, include_resonance=True)
        count = count_antinodes_withing_grid(grid, locations)
        self.assertEqual(count, 34, "Expected 34 antinodes within the grid")

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAdventDay8)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == '__main__':
    main()
