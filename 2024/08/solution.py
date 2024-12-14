def parse_data(file_path):
    with open(file_path, "r") as file:
        data = file.read()

    data = data.split("\n")
    grid = []
    for line in data:
        grid.append([x for x in line])
    return grid

def calculate_distance(antenna1, antenna2):
    return (antenna1[0] - antenna2[0], antenna1[1] - antenna2[1])

def calculate_antinodes_distances(antennas):
    antinodes = []
    for frequency, coordinates in antennas.items():
        for i in range(len(coordinates)):
            for j in range(i + 1, len(coordinates)):
                coordinate1 = coordinates[i]
                coordinate2 = coordinates[j]
                antinodes.append((frequency, coordinate1, coordinate2, calculate_distance(coordinate1, coordinate2)))
    return antinodes

def calculate_max_range(grid):
    return len(grid), len(grid[0])

def place_antinodes(antinodes, max_range, include_resonance=False):
    locations = set()
    for antinode in antinodes:
        frequency, coordinate1, coordinate2, distance = antinode
        antinode1 = (coordinate1[0] + distance[0], coordinate1[1] + distance[1])
        antinode2 = (coordinate2[0] - distance[0], coordinate2[1] - distance[1])
        locations.add(antinode1)
        locations.add(antinode2)
        if include_resonance:
            locations = place_resonance(locations, antinode1, distance, max_range)
            locations = place_resonance(locations, antinode2, distance, max_range)
            
    return locations

def place_resonance(locations, antinode, distance, max_range, visited=None):
    if visited is None:
        visited = set()
    
    if antinode in visited:
        return locations
    visited.add(antinode)
    
    # positive direction
    resonance = antinode[0] + distance[0], antinode[1] + distance[1]
    if 0 <= resonance[0] < max_range[0] and 0 <= resonance[1] < max_range[1] and resonance not in visited:
        locations.add(resonance)
        locations = place_resonance(locations, resonance, distance, max_range, visited)
    
    # negative direction
    resonance = antinode[0] - distance[0], antinode[1] - distance[1]
    if 0 <= resonance[0] < max_range[0] and 0 <= resonance[1] < max_range[1] and resonance not in visited:
        locations.add(resonance)
        locations = place_resonance(locations, resonance, distance, max_range, visited)
    
    return locations

def get_coordinates_of_antennas(grid):
    antennas = {}
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell != ".":
                if cell not in antennas:
                    antennas[cell] = []
                antennas[cell].append((i, j))
    return antennas

def count_antinodes_withing_grid(grid, locations):
    count = 0
    for location in locations:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) == location:
                    count += 1
    return count

def main():
    grid = parse_data("08/input.txt")
    max_range = calculate_max_range(grid)
    print(f"Max range: {max_range}")
    antennas = get_coordinates_of_antennas(grid)
    antinode_locations = calculate_antinodes_distances(antennas)
    locations = place_antinodes(antinode_locations, max_range)
    locations_with_resonance = place_antinodes(antinode_locations, max_range, include_resonance=True)
    print(count_antinodes_withing_grid(grid, locations))
    print(count_antinodes_withing_grid(grid, locations_with_resonance))

if __name__ == "__main__":
    main()