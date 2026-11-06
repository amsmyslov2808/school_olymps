TYPE_OPEN = ["(", "[", "{"]
TYPE_CLOSE = [")", "]", "}"]
memo = {}

def request_bracket(N) -> int:
    if not N:
        return 0
    if N in memo:
        return memo[N]
    first_bracket = N[0]
    if len(N) == 1:
        return 1
    if N[1] in TYPE_CLOSE:
        if first_bracket == TYPE_OPEN[TYPE_CLOSE.index(N[1])]:
            if len(N[2:]) != 0:
                memo[N] = request_bracket(N[2:])
                return memo[N]

    result = request_bracket(N[1:]) + 1

    for i in range(len(N) - 1, 0, -1):
        if N[i] in TYPE_CLOSE:
            if first_bracket == TYPE_OPEN[TYPE_CLOSE.index(N[i])]:
                current = request_bracket(N[i + 1:]) + request_bracket(N[1:i])
                if current < result:
                    result = current

    memo[N] = result
    return result

N = input()
print(request_bracket(N))