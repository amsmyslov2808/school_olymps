def convert_to(number, base):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits):
        return None  
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result

N = int(input())
result_sist = []
for i in range(2, 37):
    if i == 1:
        continue
    
    N_i = convert_to(N, i)

    if str(N_i) == str(N_i)[::-1]:
        result_sist.append(i)

if not result_sist:
    print("none")
else:
    if len(result_sist) > 1:
        print("multiple")
        for item in result_sist:
            print(item, end=' ')
    else:
        print("unique")
        print(result_sist[0])