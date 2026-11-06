def isValid(s):
    stack = []
    for item in s:
        if item == "(" or item == "{" or item == "[":
            stack.append(item)
        else:
            if len(stack) == 0:
                return False

            last_quote = stack.pop()

            if item == ")" and last_quote != "(":
                return False
            if item == "}" and last_quote != "{":
                return False
            if item == "]" and last_quote != "[":
                return False

    if len(stack) == 0:
        return True
    else:
        return False


print(isValid(")("))
