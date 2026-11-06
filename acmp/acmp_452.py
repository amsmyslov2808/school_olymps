def get_fib_basis(max_value: int) -> list:
    fib = [1, 2]
    while fib[-1] < max_value:
        fib.append(fib[-1] + fib[-2])
    return fib

def translate(number: int) -> int:
    s = str(number)[::-1]
    fib = [1, 2]
    while len(fib) < len(s):
        fib.append(fib[-1] + fib[-2])
        
    result_number = 0
    for i in range(len(s)):
        if s[i] == "1":
            result_number += fib[i]
    return result_number

def translate_out(number: int) -> str:
    if number == 0:
        return "0"
        
    fibon_numb = get_fib_basis(number)
    if fibon_numb[-1] > number:
        fibon_numb.pop()
        
    fibon_numb.reverse()
    result = []
    for f in fibon_numb:
        if number >= f:
            result.append("1")
            number -= f
        else:
            result.append("0")
    return "".join(result)

        
N = int(input())
M = int(input())

print(translate_out(translate(N) + translate(M)))