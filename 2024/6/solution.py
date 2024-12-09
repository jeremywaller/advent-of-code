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

def main():
    data = parse_data("6/input.txt")
    data_as_matrix, _, _ = parse_data_as_matrix(data)
    guard_position = find_guard_in_matrix(data_as_matrix)
    move_guard(data_as_matrix, guard_position)
    print(f"Part 1: {count_visited_cells(data_as_matrix)}")

if __name__ == "__main__":
    main()
