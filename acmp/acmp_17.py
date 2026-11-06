n = int(input())

numbers = list(map(int, input().split()))

total_length = n - 1

for sectors in range(1, total_length + 1):
    if total_length % sectors == 0:

        match_found = True
        for i in range(total_length - sectors):
            if numbers[i] != numbers[i + sectors]:
                match_found = False
                break

        if match_found:
            print(sectors)
            break