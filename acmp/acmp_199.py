NUMBER = ["I", "V", "X", "L", "C", "D", "M"]
TRANSCRIPT_NUMBER = [1, 5, 10, 50, 100, 500, 1000]
ROMAN = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
         (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
         (5, "V"), (4, "IV"), (1, "I")]

def divide_number(string) -> list:
    for i in range(len(string)):
        if string[i] == "/":
            return [string[:i], string[i + 1:]]
    return None 

def check_correct(number: str) -> bool:
    if number == "":  # пустая часть дроби
        return False
    for item in number:
        if item not in NUMBER:
            return False
    return True

def get_decimal_number_system(number_str: str) -> int:
        number = list(number_str)
        number.reverse()
        result = 0
        last_used = False
        for i in range(len(number)):
            if last_used:
                last_used = False
                continue
            if i < len(number) - 1:
                if TRANSCRIPT_NUMBER[NUMBER.index(number[i])] <= TRANSCRIPT_NUMBER[NUMBER.index(number[i + 1])]:
                    result += TRANSCRIPT_NUMBER[NUMBER.index(number[i])]
                else:
                    result += TRANSCRIPT_NUMBER[NUMBER.index(number[i])] - TRANSCRIPT_NUMBER[NUMBER.index(number[i + 1])]
                    last_used = True
            if i == len(number) - 1:
                if last_used:
                    last_used = False
                    continue
                result += TRANSCRIPT_NUMBER[NUMBER.index(number[i])]
        return result

def get_result_decemal(number1, number2):
    number1, number2 = int(number1), int(number2)
    if number1 % number2 == 0:
        return int(number1 / number2)
    for i in range(min(number1, number2), 0, -1):
        if number1 % i == 0 and number2 % i == 0 and i != 0:
            return f"{int(number1 / i)}/{int(number2 / i)}"

def decemal_into_rim(number:int) -> str:
    result = ""
    for value, symbol in ROMAN:
        while number >= value:
            result += symbol
            number -= value
    return result


N = input().strip()

parts = divide_number(N)

if parts is not None and check_correct(parts[0]) and check_correct(parts[1]):
    a = get_decimal_number_system(parts[0])
    b = get_decimal_number_system(parts[1])
    result = get_result_decemal(a, b)
    if isinstance(result, int):
        print(decemal_into_rim(result))
    else:
        left, right = result.split("/")
        print(decemal_into_rim(int(left)) + "/" + decemal_into_rim(int(right)))
else:
    print("ERROR")