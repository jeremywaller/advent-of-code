import sys

limit = 10000

def parse_data(file_path):
    with open(file_path, 'r') as f:
        return f.read()
    
def parse_data_as_matrix(data):
    matrix = []
    for line in data.split("\n"):
        if line.strip():
            matrix.append(list(line))
            print(line)
    return matrix, len(matrix), len(matrix[0])

def find_guard_in_matrix(matrix):
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == UP or col == DOWN or col == LEFT or col == RIGHT:
                return i, j
    return None

LEFT = "<"
RIGHT = ">"
UP = "^"
DOWN = "v"
VISITED = "X"
BLOCKED = "#"
LEFT_COORDINATES = (0, -1)
RIGHT_COORDINATES = (0, 1)
UP_COORDINATES = (-1, 0)
DOWN_COORDINATES = (1, 0)
VALID_MOVE_AREAS = [".", "X"]

def is_blocked(matrix, position):
    return matrix[position[0]][position[1]] == BLOCKED

def is_valid_move_area(matrix, position):
    return matrix[position[0]][position[1]] in VALID_MOVE_AREAS

def move_forward(matrix, guard_position):
    try:
        current_position = matrix[guard_position[0]][guard_position[1]]
        #up
        if current_position == UP and \
        not is_blocked(matrix, (guard_position[0]+UP_COORDINATES[0], guard_position[1]+UP_COORDINATES[1])):
            matrix[guard_position[0]][guard_position[1]] = VISITED
            next_position = (guard_position[0]+UP_COORDINATES[0], guard_position[1]+UP_COORDINATES[1])
            next_position_is_empty = is_valid_move_area(matrix, next_position)
            if next_position_is_empty:
                matrix[next_position[0]][next_position[1]] = UP
            return next_position_is_empty
        #right
        if current_position == RIGHT and \
        not is_blocked(matrix, (guard_position[0]+RIGHT_COORDINATES[0], guard_position[1]+RIGHT_COORDINATES[1])):
            #print("right")
            matrix[guard_position[0]][guard_position[1]] = VISITED
            next_position = (guard_position[0]+RIGHT_COORDINATES[0], guard_position[1]+RIGHT_COORDINATES[1])
            next_position_is_empty = is_valid_move_area(matrix, next_position)
            if next_position_is_empty:
                matrix[next_position[0]][next_position[1]] = RIGHT
            return next_position_is_empty
        #down
        if current_position == DOWN and \
        not is_blocked(matrix, (guard_position[0]+DOWN_COORDINATES[0], guard_position[1]+DOWN_COORDINATES[1])):
            matrix[guard_position[0]][guard_position[1]] = VISITED
            next_position = (guard_position[0]+DOWN_COORDINATES[0], guard_position[1]+DOWN_COORDINATES[1])
            next_position_is_empty = is_valid_move_area(matrix, next_position)
            if next_position_is_empty:
                matrix[next_position[0]][next_position[1]] = DOWN
            return next_position_is_empty
        #left
        if current_position == LEFT and \
        not is_blocked(matrix, (guard_position[0]+LEFT_COORDINATES[0], guard_position[1]+LEFT_COORDINATES[1])):
            matrix[guard_position[0]][guard_position[1]] = VISITED
            next_position = (guard_position[0]+LEFT_COORDINATES[0], guard_position[1]+LEFT_COORDINATES[1])
            next_position_is_empty = is_valid_move_area(matrix, next_position)
            if next_position_is_empty:
                matrix[next_position[0]][next_position[1]] = LEFT
            return next_position_is_empty
        return False
    except IndexError:
        matrix[guard_position[0]][guard_position[1]] = VISITED
        return False

def combind_matrix_and_print(matrix):
    for row in matrix:
        print("".join(row))

def move_guard(matrix, guard_position):
    while move_forward(matrix, guard_position):
        pass

    #rotate 90 degrees
    if matrix[guard_position[0]][guard_position[1]] == UP:
        matrix[guard_position[0]][guard_position[1]] = RIGHT
    elif matrix[guard_position[0]][guard_position[1]] == RIGHT:
        matrix[guard_position[0]][guard_position[1]] = DOWN
    elif matrix[guard_position[0]][guard_position[1]] == DOWN:
        matrix[guard_position[0]][guard_position[1]] = LEFT
    elif matrix[guard_position[0]][guard_position[1]] == LEFT:
        matrix[guard_position[0]][guard_position[1]] = UP

    #combind_matrix_and_print(matrix)
    guard_position = find_guard_in_matrix(matrix)

    if guard_position is not None:
        move_guard(matrix, guard_position)
    else:
        print("Guard not found")

def count_visited_cells(matrix):
    return sum(row.count(VISITED) for row in matrix)

def main():
    sys.setrecursionlimit(limit)
    data = parse_data("6/input.txt")
    data_as_matrix, matrix_height, matrix_width = parse_data_as_matrix(data)
    guard_position = find_guard_in_matrix(data_as_matrix)
    move_guard(data_as_matrix, guard_position)
    print(count_visited_cells(data_as_matrix))

if __name__ == "__main__":
    main()