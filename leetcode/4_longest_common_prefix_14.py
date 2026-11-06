def longestCommonPrefix(strs):
    prefix = ""

    current_index = -1

    while True:
        current_index += 1

        if current_index > len(strs[0]) - 1:
            return prefix

        current_letter = strs[0][current_index]
        count_same = 0

        for item in strs:
            if current_index <= len(item) - 1:
                if item[current_index] == current_letter:
                    count_same += 1

        if count_same == len(strs):
            prefix += current_letter
        else:
            return prefix


print(longestCommonPrefix(["flower", "flow", "flight"]))
