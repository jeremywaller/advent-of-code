#!/usr/bin/env python3
import unittest
from solution import parse_data, evaluate_equation

class TestAdventDay7(unittest.TestCase):
    def test_evaluate_equation_part1(self):
        data = parse_data("07/test_input.txt")
        self.assertEqual(sum(int(item["answer"]) for item in data if evaluate_equation(item["answer"], item["equation"])), 3749, "Expected 3,749")

    def test_evaluate_equation_part2(self):
        data = parse_data("07/test_input.txt")
        self.assertEqual(sum(int(item["answer"]) for item in data if evaluate_equation(item["answer"], item["equation"], True)), 11387, "Expected 11,387")

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAdventDay7)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == '__main__':
    main() 