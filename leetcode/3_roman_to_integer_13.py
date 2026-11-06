def romanToInt(s: str):
    numbers = [["I", "V", "X", "L", "C", "D", "M"], [1, 5, 10, 50, 100, 500, 1000]]

    result_number = 0

    reverse_str = s[::-1]  # LXV

    prev_letter_index = -1
    cur_letter_index = -1

    for letter in reverse_str:
        cur_letter_index = numbers[0].index(letter)

        if cur_letter_index < prev_letter_index:
            result_number -= numbers[1][cur_letter_index]
        else:
            result_number += numbers[1][cur_letter_index]

        prev_letter_index = cur_letter_index

    return result_number


print(romanToInt("MCMXCIV"))
