def remove_match_char(list1, list2):
    """
    Removes matching characters from both lists and returns a new list
    with remaining characters separated by "*".
    """
    for i in range(len(list1)):
        if list1[i] in list2:
            c = list1[i]
            list1.remove(c)
            list2.remove(c)
            # Return combined list with a "*" separator and True indicating a match was found
            return [list1 + ["*"] + list2, True]

    # No matches found; return combined list with a "*" separator and False
    return [list1 + ["*"] + list2, False]


if __name__ == "__main__":
    # Player 1 input
    p1 = input("Enter the first name: ")
    p1 = p1.lower().replace(" ", "")
    p1_list = list(p1)

    # Player 2 input
    p2 = input("Enter the second name: ")
    p2 = p2.lower().replace(" ", "")
    p2_list = list(p2)

    # Process until no more matches are found
    process = True
    while process:
        ret_list = remove_match_char(p1_list, p2_list)
        cot_list = ret_list[0]
        flag = ret_list[1]

        # Split the list at the "*" separator
        if "*" in cot_list:
            star_index = cot_list.index("*")
            p1_list = cot_list[:star_index]
            p2_list = cot_list[star_index + 1:]
        else:
            p1_list = cot_list
            p2_list = []

        process = flag

    # Calculate the final count of remaining characters
    count = len(p1_list) + len(p2_list)

    # List of possible relationship statuses
    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    # Determine the relationship status using the remaining count
    while len(result) > 1:
        split_index = (count % len(result) - 1)
        if split_index >= 0:
            right = result[split_index + 1:]
            left = result[:split_index]
            result = right + left
        else:
            result = result[:len(result) - 1]

    # Print the final relationship status
    print("Relationship status:", result[0])
