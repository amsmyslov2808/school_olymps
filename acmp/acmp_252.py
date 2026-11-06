def reset_fun(c: list):
    one_ed = c[1][-1]
    if one_ed == "g":
        unit_coef = 1
    elif one_ed == "p":
        unit_coef = 16380
    elif one_ed == "t":
        unit_coef = 1000000

    if len(c[1]) > 1:
        two_ed = c[1][:-1]
        if two_ed == "m":
            prefix_coef = 1
        elif two_ed == "k":
            prefix_coef = 1_000_000
        elif two_ed == "M":
            prefix_coef = 1_000_000_000
        elif two_ed == "G":
            prefix_coef = 1_000_000_000_000
    else:
        prefix_coef = 1000 

    return int(c[0]) * unit_coef * prefix_coef


N=int(input())
a=[]
for i in range(N):
    mass,ed=input().split()
    mass=int(mass)
    a.append([mass,ed])

a=sorted(a,key=reset_fun)
for i in a:
    print(i[0],i[1])
