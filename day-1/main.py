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
        left_list.append(int(left))
        right_list.append(int(right))

    # Sort each column
    left_list.sort()
    right_list.sort()
    return left_list, right_list


def calc_total_distance(left_list, right_list):
    """Determines what is the total distance between left and right column sorted"""
    total_distance = 0
    for idx, _ in enumerate(left_list):
        total_distance += abs(left_list[idx] - right_list[idx])
        print(
            f"{idx}\t:\t[left: {left_list[idx]}] [right: {right_list[idx]}]\t-\t{abs(int(left_list[idx]) - int(right_list[idx]))}\t-\t{total_distance}"
        )
    print(f"Total Distance: {total_distance}")


def calc_sim_score(left_list, right_list):
    """Calculate a total similarity score by adding up each number
    in the left list after multiplying it by the number of times
    that number appears in the right list.
    """
    similarity_score = 0
    for l_row_item in left_list:
        # Multiply the row item on the left column
        #   by the # times it appears on the right column
        similarity_score += l_row_item * right_list.count(l_row_item)
    print(f"Similarity Score: {similarity_score}")


if __name__ == "__main__":
    left_list, right_list = readInput("./input.txt")
    # calc_total_distance(left_list, right_list)
    calc_sim_score(left_list, right_list)
