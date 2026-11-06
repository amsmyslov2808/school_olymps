x, y, z, w = map(int, input().split())

count_x = w // x + 1
count_y = w // y + 1
count_z = w // z + 1

count_variants = 0

# for i in range(count_x):
#     for j in range(count_y):
#         for k in range(count_z):
#             if x * i + j * y + k * z == w:
#                 count_variants += 1

for i in range(count_x):
    for j in range(count_y):
        k = (w - i * x - j * y) // z
        if k >= 0:
            if x * i + j * y + k * z == w:
                count_variants += 1

print(count_variants)
