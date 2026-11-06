all = list(map(int, input().split()))
go = True

result = min(all[0] // 2, all[1] // 6, all[2]) 

print(result)
