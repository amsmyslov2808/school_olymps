team_1 = 0
team_2 = 0
for _ in range(4):
    all = list(map(int, input().split()))
    team_1 += all[0]
    team_2 += all[1]
    all.clear()

if team_1 > team_2:
    print("1")
elif team_1 < team_2:
    print("2")
else:
    print("DRAW")