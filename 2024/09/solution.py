class DiskDefragmenter:
    def __init__(self, disk_map):
        self.disk_map = disk_map
        self.blocks = []
        self.parse_disk_map()

    def parse_disk_map(self):
        file_id = 0
        for i, length in enumerate(self.disk_map):
            length = int(length)
            if i % 2 == 0:  # File blocks
                self.blocks.extend([file_id] * length)
                file_id += 1
            else:  # Free space blocks
                self.blocks.extend(['.'] * length)
    
    def print_state(self):
        print(''.join(str(x) if x != '.' else '.' for x in self.blocks))
    
    def compact_part1(self):
        moved = True
        while moved:
            moved = False
            # Find rightmost file block
            for i in range(len(self.blocks)-1, -1, -1):
                if self.blocks[i] != '.':
                    # Find leftmost free space
                    for j in range(i):
                        if self.blocks[j] == '.':
                            # Move block
                            self.blocks[j] = self.blocks[i]
                            self.blocks[i] = '.'
                            moved = True
                            break
                    break
                            
    def compact_part2(self):
        # Get unique file IDs and sort in descending order
        file_ids = sorted(set(x for x in self.blocks if x != '.'), reverse=True)
        
        for file_id in file_ids:
            # Get file size and current positions
            positions = [i for i, x in enumerate(self.blocks) if x == file_id]
            file_size = len(positions)
            if not positions:
                continue
                
            # Find leftmost valid position for the whole file
            best_start = None
            free_count = 0
            last_good_start = None
            
            for i in range(min(positions)):
                if self.blocks[i] == '.':
                    if free_count == 0:
                        last_good_start = i
                    free_count += 1
                    if free_count >= file_size:
                        best_start = last_good_start
                        break
                else:
                    free_count = 0
                    
            # If we found a valid position, move the file
            if best_start is not None:
                # Clear old positions
                for pos in positions:
                    self.blocks[pos] = '.'
                # Place file in new position
                for i in range(file_size):
                    self.blocks[best_start + i] = file_id
            
    def calculate_checksum(self):
        return sum(pos * block for pos, block in enumerate(self.blocks) 
                  if block != '.')

def solve_part1(disk_map):
    defrag = DiskDefragmenter(disk_map)
    defrag.compact_part1()
    return defrag.calculate_checksum()

def solve_part2(disk_map):
    defrag = DiskDefragmenter(disk_map)
    defrag.compact_part2()
    return defrag.calculate_checksum()

def main():
    with open("09/input.txt", "r") as file:
        disk_map = file.read()
    print(f"Part 1 solution: {solve_part1(disk_map)}")
    print(f"Part 2 solution: {solve_part2(disk_map)}")

if __name__ == "__main__":
    main()