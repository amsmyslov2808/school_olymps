s1, s2, s3 = map(int, input().split())

min_s = min(s1, s2, s3)
max_s = max(s1, s2, s3)

delta = max_s - min_s

print(delta)
