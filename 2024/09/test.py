import unittest
from solution import parse_data, parse_disk_map, visualize_disk, defragment, calculate_checksum

class TestAdventDay9(unittest.TestCase):
    def setUp(self):
        # Read from test_input.txt
        self.test_disk_map = parse_data("09/test_input.txt")
        
    def test_complete_defragmentation(self):
        # Step 1: Test parsing disk map
        disk_details = parse_disk_map(self.test_disk_map)
        defragment(disk_details)
        checksum = calculate_checksum(disk_details)
        self.assertEqual(checksum, 1928)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAdventDay9)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == '__main__':
    main()
