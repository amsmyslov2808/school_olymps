
time1 = input().strip().split(":")
time2 = input().strip().split()    


h1, m1 = map(int, time1)
h2, m2 = map(int, time2)

total_minutes = (h1 * 60 + m1) + (h2 * 60 + m2)

arrival_hours = (total_minutes // 60) % 24
arrival_minutes = total_minutes % 60

print(f"{arrival_hours:02d}:{arrival_minutes:02d}")