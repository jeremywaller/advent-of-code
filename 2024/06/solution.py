LEFT = "<"
RIGHT = ">"
UP = "^"
DOWN = "v"
VISITED = "X"
BLOCKED = "#"

VALID_MOVE_AREAS = [".", "X"]
DIRECTIONS = [UP, RIGHT, DOWN, LEFT]

DIRECTION_OFFSETS = {
    UP:    (-1, 0),
    RIGHT: (0, 1),
    DOWN:  (1, 0),
    LEFT:  (0, -1)
}

def parse_data(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def parse_data_as_matrix(data):
    matrix = [list(line) for line in data.split("\n") if line.strip()]
    return matrix, len(matrix), len(matrix[0]) if matrix else 0

def find_guard_in_matrix(matrix):
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col in DIRECTIONS:
                return (i, j)
    return None

def is_blocked(matrix, position):
    return matrix[position[0]][position[1]] == BLOCKED

def is_valid_move_area(matrix, position):
    return matrix[position[0]][position[1]] in VALID_MOVE_AREAS

def in_bounds(matrix, position):
    rows = len(matrix)
    cols = len(matrix[0])
    return 0 <= position[0] < rows and 0 <= position[1] < cols

def move_forward(matrix, guard_position):
    i, j = guard_position
    direction = matrix[i][j]
    offset = DIRECTION_OFFSETS[direction]
    next_pos = (i + offset[0], j + offset[1])

    if not in_bounds(matrix, next_pos):
        matrix[i][j] = VISITED
        return None

    if is_blocked(matrix, next_pos):
        return None

    if is_valid_move_area(matrix, next_pos):
        matrix[i][j] = VISITED
        matrix[next_pos[0]][next_pos[1]] = direction
        return next_pos

    return None

def rotate_direction(matrix, guard_position):
    i, j = guard_position
    direction = matrix[i][j]
    current_index = DIRECTIONS.index(direction)
    new_direction = DIRECTIONS[(current_index + 1) % len(DIRECTIONS)]
    matrix[i][j] = new_direction
    
def move_guard(matrix, guard_position):
    while guard_position is not None:
        next_pos = move_forward(matrix, guard_position)
        while next_pos is not None:
            guard_position = next_pos
            next_pos = move_forward(matrix, guard_position)

        guard_position = find_guard_in_matrix(matrix)
        if guard_position is None:
            break

        rotate_direction(matrix, guard_position)
        guard_position = find_guard_in_matrix(matrix)

def count_visited_cells(matrix):
    return sum(row.count(VISITED) for row in matrix)

def find_guard_route(matrix):
    guard_position = find_guard_in_matrix(matrix)
    move_guard(matrix, guard_position)

    return count_visited_cells(matrix)

def find_visited_cells(matrix):
    visited_cells = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == VISITED:
                visited_cells.add((i, j))
    return visited_cells

def test_blocker_position(original_matrix, blocker_pos):
    matrix = [row[:] for row in original_matrix]
    matrix[blocker_pos[0]][blocker_pos[1]] = BLOCKED
    
    guard_position = find_guard_in_matrix(matrix)
    if guard_position is None:
        return False
        
    visited_states = set()
    while guard_position is not None:
        current_state = (guard_position, matrix[guard_position[0]][guard_position[1]])
        if current_state in visited_states:
            return True
        visited_states.add(current_state)
        
        next_pos = move_forward(matrix, guard_position)
        if next_pos is not None:
            guard_position = next_pos
            continue
            
        guard_position = find_guard_in_matrix(matrix)
        if guard_position is None:
            return False
        rotate_direction(matrix, guard_position)
        
    return False

def count_successful_blockers(matrix):
    guard_position = find_guard_in_matrix(matrix)
    matrix_copy = [row[:] for row in matrix]
    move_guard(matrix_copy, guard_position)
    visited_cells = find_visited_cells(matrix_copy)
    
    successful_blockers = 0
    total_cells = len(visited_cells)
    for i, cell in enumerate(visited_cells, 1):
        if test_blocker_position(matrix, cell):
            successful_blockers += 1
        if i % 10 == 0:
            print(f"Progress: {i}/{total_cells} cells checked. Found {successful_blockers} successful blockers so far.")
            
    return successful_blockers

def main():
    data = parse_data("06/input.txt")
    data_as_matrix, _, _ = parse_data_as_matrix(data)
    
    # Part 1
    matrix_copy = [row[:] for row in data_as_matrix]
    guard_position = find_guard_in_matrix(matrix_copy)
    move_guard(matrix_copy, guard_position)
    print(f"Part 1: {count_visited_cells(matrix_copy)}")
    
    # Part 2
    successful_blockers = count_successful_blockers(data_as_matrix)
    print(f"Part 2: {successful_blockers}")

if __name__ == "__main__":
    main()
