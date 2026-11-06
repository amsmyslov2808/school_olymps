l, w, h = list(map(int, input().split()))
result = 0

wall_area = 2 * (l + w) * h

cans_needed = (wall_area + 15) // 16

print(cans_needed)