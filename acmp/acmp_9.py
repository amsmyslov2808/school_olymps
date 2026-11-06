n = int(input())
numbers = list(map(int, input().split()))

first_result = sum(x for x in numbers if x > 0)

min_idx = numbers.index(min(numbers))
max_idx = numbers.index(max(numbers))

lo, hi = sorted([min_idx, max_idx]) 
between = numbers[lo + 1 : hi]       
second_result = 1
for x in between:
    second_result *= x

print(first_result, second_result)