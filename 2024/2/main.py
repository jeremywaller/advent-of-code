def parse_data(filename):
    with open(filename, 'r') as file:
        return [list(map(int, line.strip().split())) for line in file]

def is_progressing_safely(list):
    difference = [list[i+1] - list[i] for i in range(len(list) - 1)]
    increasing = all(1 <= diff <= 3 for diff in difference)
    decreasing = all(-3 <= diff <= -1 for diff in difference)
    return increasing or decreasing

def remove_bad_levels_and_test(list):
    # remove first element and test
    if is_progressing_safely(list[1:]):
        return True
    # remove last element and test
    elif is_progressing_safely(list[:-1]):
        return True
    else:
        # remove middle elements and test
        for i in range(1, len(list) - 1):
            if is_progressing_safely(list[:i] + list[i+1:]):
                return True
        return False

def is_safe(list, remove_bad_levels=False):
    if len(list) > 2 and is_progressing_safely(list):
        return True
    elif remove_bad_levels:
        return remove_bad_levels_and_test(list)
    else:
        return False

def count_safe_lists(data, remove_bad_levels=False): 
    return sum(1 for line in data if is_safe(line, remove_bad_levels))

def main():
    data = parse_data("2/input.txt")
    print(f'Part 1: {count_safe_lists(data)}')
    print(f'Part 2: {count_safe_lists(data, True)}')

if __name__ == "__main__":
    main()
