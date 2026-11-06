time = list(map(int, input().split()))
time_normal = 0
time_no_normal = 0

if time[3] > time[0]:
    time_normal = time[0] * time[1]
    time_no_normal = (time[3] - time[0]) * time[2]
    print(time_normal + time_no_normal)
else:
    print(time[3] * time[1])