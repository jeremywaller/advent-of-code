ALLOWED_OPERATIONS = ["+", "*"]

OPERATORS = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y
}

def parse_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

    data_set = []

    for line in data.split("\n"):
        answer, equation = line.split(":")
        data_set.append({
            "answer": int(answer),
            "equation": [int(x) for x in equation.strip().split(" ")] 
        })
    return data_set

def evaluate_equation(answer, equation):
    if equation[0] > answer:
        return False
    
    if len(equation) == 1:
        return equation[0] == answer
    
    if(evaluate_equation(answer, [equation[0] + equation[1]] + equation[2:])):
        return True
    if(evaluate_equation(answer, [equation[0] * equation[1]] + equation[2:])):
        return True
    return False

def main():
    data = parse_data("7/input.txt")
    total = len(data)
    results = sum(item["answer"] for item in data if evaluate_equation(item["answer"], item["equation"]))
    
    print(f'Part 1: {results}')

if __name__ == "__main__":
    main()