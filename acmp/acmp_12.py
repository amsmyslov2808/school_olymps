n = int(input())
coords = []
got_it = 0
for i in range(n):
    x, y, x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    coords.append([x, y, x1, y1, x2, y2, x3, y3, x4, y4])

def is_point_in_rectangle(x, y, x1, y1, x2, y2, x3, y3, x4, y4):
    side_one_x = x2 - x1
    side_one_y = y2 - y1
    side_two_x = x4 - x1
    side_two_y = y4 - y1
    to_point_x = x - x1
    to_point_y = y - y1
    proj_1 = to_point_x*side_one_x + to_point_y*side_one_y
    proj_2 = to_point_x*side_two_x + to_point_y*side_two_y
    len1_sq = side_one_x**2 + side_one_y**2
    len2_sq = side_two_x**2 + side_two_y**2
    ok1 = 0 <= proj_1 <= len1_sq
    ok2 = 0 <= proj_2 <= len2_sq
    return ok1 and ok2


for i in range(n):
    x, y, x1, y1, x2, y2, x3, y3, x4, y4 = coords[i]
    if is_point_in_rectangle(x, y, x1, y1, x2, y2, x3, y3, x4, y4):
        got_it += 1

print(got_it)