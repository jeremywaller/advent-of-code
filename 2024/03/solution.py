
def parse_data(filename):
    with open(filename, 'r') as file:
        return file.read().strip()
    
def find_mul_instructions(input_string, enforce_do_instructions=False):
    # I refuse to use regex here
    i = 0
    n = len(input_string)
    mul_instructions = []
    while i < n:
        if enforce_do_instructions and input_string[i:i+7] == "don't()":
            i += 7
            
            while i < n and input_string[i:i+4] != "do()":
                i += 1
                continue

        if input_string[i:i+4] == "mul(":
            i += 4
            # parse first number
            start = i
            while input_string[i].isdigit():
                i += 1
            if i > start:
                first_number = int(input_string[start:i])
            else:
                continue

            # parse comma
            if input_string[i] == ",":
                i += 1
            else:
                continue

            # parse second number
            start = i
            while input_string[i].isdigit():
                i += 1
            if i > start:
                second_number = int(input_string[start:i])
            else:
                continue
                
            # confirm closing parenthesis
            if input_string[i] == ")":
                i += 1
            else:
                continue
            
            # return the two numbers
            mul_instructions.append((first_number, second_number))
        else:
            i += 1

    return mul_instructions

def perform_mul_instructions(mul_instructions):
    result = 0
    for first_number, second_number in mul_instructions:
        result += first_number * second_number
    return result

def get_result(input_string, enforce_do_instructions=False):
    mul_instructions = find_mul_instructions(input_string, enforce_do_instructions)
    return perform_mul_instructions(mul_instructions)

def main():
    data = parse_data("3/input.txt")
    print(f'Part 1: {get_result(data)}')
    print(f'Part 2: {get_result(data, enforce_do_instructions=True)}')

if __name__ == "__main__":
    main()