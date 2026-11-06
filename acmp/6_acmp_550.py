# k = int(input())

# if (k % 400 == 0) or (k % 4 == 0 and k % 100 != 0):
#     print(f"12/09/{k:04d}")
# else:
#     print(f"13/09/{k:04d}")

year = int(input())

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"12/09/{(4-len(str(year)))*'0'+str(year)}")
else:
    print(f"13/09/{(4-len(str(year)))*'0'+str(year)}")
