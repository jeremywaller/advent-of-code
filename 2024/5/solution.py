from graphlib import TopologicalSorter, CycleError

def parse_data(file_path):
    file_data = []
    with open(file_path, 'r') as file:
        file_data = file.read().strip().split('\n\n')
    part_1_data = [tuple(map(int, row.split('|'))) for row in file_data[0].split('\n')]
    part_2_data = [list(map(int, row.split(','))) for row in file_data[1].split('\n')]
    return part_1_data, part_2_data

def get_middle_pages_for_sorted_updates(update_rules, updates):
    middle_pages_correctly_sorted = []
    middle_pages_incorrectly_sorted = []
    for update in updates:
        update_rule = []
        # find all the rules that apply to the current update
        for page in update:
            for rule in update_rules:
                if rule[0] == page and rule[1] in update:
                    update_rule.append(rule)

        # Create a graph for topological sorting
        graph = {}
        for page in update:
            graph[page] = set()
        
        # Add edges based on rules
        for rule in update_rule:
            before, after = rule
            graph[before].add(after)

        # Use TopologicalSorter to get the ordering
        try:
            ts = TopologicalSorter(graph)
            sorted_pages = list(ts.static_order())
            # Filter to only include pages in the current update
            sorted_update = [p for p in sorted_pages if p in update]
            sorted_update.reverse()
            middle_index = len(sorted_update) // 2
            middle_page = sorted_update[middle_index]
            if sorted_update == update:
                middle_pages_correctly_sorted.append(middle_page)
            else:
                middle_pages_incorrectly_sorted.append(middle_page)
        except CycleError:
            print(f"Cycle detected in update {update}")
    print(f"Middle pages correctly sorted: {middle_pages_correctly_sorted}")
    print(f"Middle pages incorrectly sorted: {middle_pages_incorrectly_sorted}")
    return sum(middle_pages_correctly_sorted), sum(middle_pages_incorrectly_sorted)

def main():
    update_rules, updates = parse_data("5/input.txt")
    correctly_sorted_sum, incorrectly_sorted_sum = get_middle_pages_for_sorted_updates(update_rules, updates)
    print(f"Sum of middle pages correctly sorted: {correctly_sorted_sum}")
    print(f"Sum of middle pages incorrectly sorted: {incorrectly_sorted_sum}")
if __name__ == "__main__":
    main()