

def parse_data(filename):
    with open(filename, "r") as file:
        data = file.readlines()
    return [tuple(map(int, line.split())) for line in data]
def split_tuple_into_two_lists(data):
    return [x for x, _ in data], [y for _, y in data]

def sort_lists_smallest_to_largest(x_list, y_list):
    return sorted(x_list), sorted(y_list)

def find_difference(x_list, y_list):
    return [abs(y - x) for x, y in zip(x_list, y_list)]

def count_number_of_occurrences(list):
    return {x: list.count(x) for x in set(list)}

def calculate_similarity_score(x_list, y_set):
    return sum([x * y_set[x] for x in x_list if x in y_set])

def puzzle_part_1(data):
    x_list, y_list = split_tuple_into_two_lists(data)
    x_list, y_list = sort_lists_smallest_to_largest(x_list, y_list)
    difference_list = find_difference(x_list, y_list)
    result = sum(difference_list)
    print(f'Part 1: {result}')
    return result

def puzzle_part_2(data):
    x_list, y_list = split_tuple_into_two_lists(data)
    y_set = count_number_of_occurrences(y_list)
    result = calculate_similarity_score(x_list, y_set)  
    print(f'Part 2: {result}')
    return result

def main():
    data = parse_data("01/input.txt")
    puzzle_part_1(data)
    puzzle_part_2(data)


if __name__ == "__main__":
    main()  
