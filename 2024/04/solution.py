def parse_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip().split('\n')
        
    # Add padding around the grid with 'Z' characters
    padded_data = []
    padding_row = 'Z' * (len(data[0]) + 2)
    
    # Add top padding rows
    for _ in range(3):
        padded_data.append(list(padding_row))
        
    # Add side padding to each row
    for row in data:
        padded_data.append(list('Z' + row + 'Z'))
        
    # Add bottom padding rows
    for _ in range(3):
        padded_data.append(list(padding_row))
        
    return padded_data

def search_grid_for_word(grid):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    word_to_find = "XMAS"
    count_found = 0
    # rows
    for i in range(len(grid)):
        # columns
        for j in range(len(grid[i])):
            if grid[i][j] == word_to_find[0]:
                for direction in directions:
                    if search_word(grid, word_to_find, 0, i, j, direction):
                        count_found += 1
    return count_found

def search_word(grid, word_to_find, starting_letter_index, i, j, direction):
    max_length = len(word_to_find) - starting_letter_index
    for k in range(max_length):
        if out_of_bounds(grid, i, j, direction, k):
            return False
        current_letter_index = (starting_letter_index + k) % len(word_to_find)
        if grid[i + k * direction[0]][j + k * direction[1]] != word_to_find[current_letter_index]:
            return False
    return True

def is_mas_pattern(grid, r, c):
    try:
        top_left = grid[r - 1][c - 1]
        top_right = grid[r - 1][c + 1]
        bottom_left = grid[r + 1][c - 1]
        bottom_right = grid[r + 1][c + 1]
        center = grid[r][c]

        # Check if center is 'A'
        if center != 'A':
            return False

        match1 = top_left + center + bottom_right
        match2 = top_right + center + bottom_left
        valid_matches = ['MAS', 'SAM']
        return match1 in valid_matches and match2 in valid_matches

    except IndexError:
        # If any index is out of bounds, it's not a valid pattern
        return False

def search_word_in_x_shape(grid):
    rows = len(grid)
    cols = len(grid[0])
    xmas_count = 0

    for r in range(rows):
        for c in range(cols):
            if is_mas_pattern(grid, r, c):
                xmas_count += 1
    return xmas_count

def out_of_bounds(grid, i, j, direction, length):
    return i + direction[0] * length < 0 or i + direction[0] * length >= len(grid) or j + direction[1] * length < 0 or j + direction[1] * length >= len(grid[0])

def main():
    data = parse_data("04/input.txt")
    data_grid = [list(row) for row in data]
    print(search_grid_for_word(data_grid))
    print(search_word_in_x_shape(data_grid))

if __name__ == "__main__":
    main()