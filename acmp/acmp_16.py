N = int(input())
result = 1
now_ladder = [0] * 40
now_ladder[0] = N


need_brake = False
i = 1
while True:
    if now_ladder[i - 1] - 1 > now_ladder[i]:
        now_ladder[i] += 1
        now_ladder[i - 1] -= 1
        result += 1
        continue
    i += 1

    for j in range(len(now_ladder)):
        if now_ladder[j] == 0:
            need_brake = True
            break
        elif now_ladder[j] - 1 == now_ladder[j + 1]:
            continue
        



