def parse_data(file_path):
    with open(file_path, "r") as file:
        return file.read()

def parse_disk_map(disk_map):
    # disk_details:
    # (id, original_position, is_file)
    disk_details = []
    file_id = 0
    free_space_id = 0
    for idx, size in enumerate(disk_map):
        if idx % 2 == 0:
            # is file
            for i in range(int(size)):
                disk_details.append((file_id, len(disk_details), True))
            file_id += 1
        else:
            # is free space
            for i in range(int(size)):
                disk_details.append((free_space_id, len(disk_details), False))
            free_space_id += 1
    return disk_details

def find_next_open_space(disk_details, start_pos=0):
    for idx in range(start_pos, len(disk_details)):
        if not disk_details[idx][2]:  # not is_file
            return idx
    return -1

def visualize_disk(disk_details):
    disk_str = ""
    for id, position, is_file in disk_details:
        if is_file:
            disk_str += str(id)
        else:
            disk_str += "."
    return disk_str

def defragment(disk_details):
    files = [(id, pos) for id, pos, is_file in disk_details if is_file]
    files.sort(key=lambda x: (x[0], x[1]), reverse=True)
    
    last_open_space = 0
    for file_id, orig_pos in files:
        open_space = find_next_open_space(disk_details, last_open_space)
        if open_space < orig_pos:
            disk_details[open_space] = (file_id, orig_pos, True)
            if open_space != orig_pos:
                disk_details[orig_pos] = (-1, -1, False)
            last_open_space = open_space + 1

def calculate_checksum(disk_details):
    #print(disk_details)
    return sum(idx * id for idx, (id, position, is_file) in enumerate(disk_details) if is_file)

def main():
    disk_map = parse_data("09/input.txt")
    disk_details = parse_disk_map(disk_map)
    defragment(disk_details)
    print(calculate_checksum(disk_details))

if __name__ == "__main__":
    main()
