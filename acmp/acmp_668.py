head, tail = [int(i) for i in input().split()]
g=0
i=0

if tail!=0 or head%2==0:
    if tail%2==1:
        i=1
        tail+=1
    i+=tail//2
    head+=tail//2
    if head%2==1:
        i+=3
        head+=1
    i+=head//2
    print(i)
else:
    print(-1)
