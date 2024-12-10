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

def evaluate_equation(answer, equation, include_concat=False):
    equation = [int(x) for x in equation]
    if equation[0] > answer:
        return False
    
    if len(equation) == 1:
        return equation[0] == answer
    
    if(evaluate_equation(answer, [equation[0] + equation[1]] + equation[2:], include_concat)):
        return True
    if(evaluate_equation(answer, [equation[0] * equation[1]] + equation[2:], include_concat)):
        return True
    if(include_concat and evaluate_equation(answer, [str(equation[0]) + str(equation[1])] + equation[2:], include_concat)):
        return True
    return False

def main():
    data = parse_data("7/input.txt")
    total = len(data)
    part1_results = sum(item["answer"] for item in data if evaluate_equation(item["answer"], item["equation"]))
    part2_results = sum(item["answer"] for item in data if evaluate_equation(item["answer"], item["equation"], True))
    
    print(f'Part 1: {part1_results}')
    print(f'Part 2: {part2_results}') 

if __name__ == "__main__":
    main()