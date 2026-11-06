# k, n = map(int, input().split())

# stroka = n % k

# stranica = 0

# if n % k == 0:
#     stranica = n // k
# else:
#     stranica = n // k + 1

# print(f"{stranica} {stroka}")

k, n = map(int, input().split())

stroka = 0
stranica = 1

while n >= k:
    n = n - k
    stranica += 1

stroka = n
if stroka == 0:
    stroka = k
    stranica -= 1

print(f"{stranica} {stroka}")


k, n = map(int, input().split())
page = (n + k - 1) // k
stroks = n % k
if stroks == 0:
    stroks = k
print(page, stroks)

k, n = map(int, input().split())
stroka = n % k if n % k != 0 else k
s = n - stroka
print(s // k + 1, stroka)
