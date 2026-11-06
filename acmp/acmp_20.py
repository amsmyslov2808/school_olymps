K = int(input())
if K <= 1:
    print(K)
else:
    N = list(map(int, input().split()))
    
    max_len = 1
    up = 1
    down = 1
    
    for i in range(1, K):
        if N[i] > N[i - 1]:
            up = down + 1
            down = 1
        elif N[i] < N[i - 1]:
            down = up + 1
            up = 1
        else:
            up = 1
            down = 1
            
        if up > max_len:
            max_len = up
        if down > max_len:
            max_len = down
            
    print(max_len)
