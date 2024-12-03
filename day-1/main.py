def readInput(input_file_path: str):
    data_str = ""
    with open(input_file_path) as input_data:
        # Trim the file a bit
        data_str = input_data.read().replace("   ", ",")

    left_list, right_list = [], []
    total_lines = data_str.split("\n")
    # Break each column into its own array
    for line in total_lines:
        left, right = line.split(",")
        left_list.append(left)
        right_list.append(right)

    # Sort each column
    left_list.sort()
    right_list.sort()

    total_distance = 0
    for idx, line in enumerate(total_lines):
        total_distance += abs(int(left_list[idx]) - int(right_list[idx]))
        print(
            f"{idx}\t:\t[left: {left_list[idx]}] [right: {right_list[idx]}]\t-\t{abs(int(left_list[idx]) - int(right_list[idx]))}\t-\t{total_distance}"
        )
    print(f"Total Distance: {total_distance}")


if __name__ == "__main__":
    readInput("./input.txt")
