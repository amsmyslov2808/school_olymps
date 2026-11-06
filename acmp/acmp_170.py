number = int(input())
itteration = 1

def itteration_in_number(itteration) -> int:
    now = 3
    now_itteration = 1
    result = 0
    while now_itteration != itteration:
        result += now
        now_itteration += 1
        now += 1
    return result

while number > itteration_in_number(itteration):
    itteration += 1
print(itteration)