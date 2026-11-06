def check(X, Y, A):
    if (
        X % A == 0 and (Y - 2) % A == 0 or
        Y % A == 0 and (X - 2) % A == 0 or
        (X - 1) % A == 0 and (Y - 1) % A == 0 or
        A <=2
    ):
        return 1
    return 0

K = int(input())
tests = [list(map(int, input().split())) for _ in range(K)]
print("".join(str(check(tests[i][0], tests[i][1], tests[i][2])) for i in range(K)))