import time
import sys

n, m = map(int, input().split())

start_time = time.perf_counter()

numbers = [0] * 10


def split_number(number):
    global numbers

    if number == 0:
        number[0] += 1
    else:
        while number != 0:
            last_digit = number % 10
            numbers[last_digit] += 1
            number = number // 10


for i in range(1, n + 1):

    stroka = ""
    for j in range(1, m + 1):
        stroka += str(i * j)

    for digit in range(10):
        numbers[digit] += stroka.count(str(digit))

for number in numbers:
    print(number)

end_time = time.perf_counter()

print(f"Время работы программы: {end_time - start_time:.6f} секунд", file=sys.stderr)
