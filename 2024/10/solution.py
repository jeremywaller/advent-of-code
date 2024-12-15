UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def parse_data(filename):
    with open(filename, "r") as file:
        data = file.read()
    return [[int(digit) for digit in line.strip()] for line in data.splitlines()]

def get_start_positions(grid):
    start_positions = []
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            if value == 0:
                start_positions.append((x, y))
    return start_positions

def get_valid_moves(grid, position):
    current_value = grid[position[1]][position[0]]
    valid_moves = []
    
    for direction in [UP, DOWN, LEFT, RIGHT]:
        new_x, new_y = position[0] + direction[0], position[1] + direction[1]
        if (0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid) and 
            grid[new_y][new_x] == current_value + 1):
            valid_moves.append(direction)
    
    return valid_moves

def navigate_trail(grid, position, visited=None):
    if visited is None:
        visited = set()
    
    if position in visited:
        return 0
    
    visited.add(position)
    
    if grid[position[1]][position[0]] == 9:
        return 1
        
    total_summits = 0
    valid_moves = get_valid_moves(grid, position)
    
    for move in valid_moves:
        new_position = (position[0] + move[0], position[1] + move[1])
        total_summits += navigate_trail(grid, new_position, visited)
    
    return total_summits

def main():
    parsed_data = parse_data("10/input.txt")
    start_positions = get_start_positions(parsed_data)
    print(start_positions)
    print(sum([navigate_trail(parsed_data, start_position) for start_position in start_positions]))

if __name__ == "__main__":
    main()