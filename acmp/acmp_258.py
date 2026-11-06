K1, M, K2, P2, N2 = [int(x) for x in input().split()]

variants = []
for X in range(1, 1001):
    if ((K2 - 1) // X) // M + 1 == P2 and ((K2 - 1) // X) % M + 1 == N2:
        p1 = ((K1 - 1) // X) // M + 1
        n1 = ((K1 - 1) // X) % M + 1
        variants.append((p1, n1))

if not variants:
    print("-1 -1") 
else:
    p_options = {v[0] for v in variants}
    n_options = {v[1] for v in variants}
    
    ans_p = list(p_options)[0] if len(p_options) == 1 else 0
    ans_n = list(n_options)[0] if len(n_options) == 1 else 0
    print(ans_p, ans_n)
