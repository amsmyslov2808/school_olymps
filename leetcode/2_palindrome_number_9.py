# https://leetcode.com/problems/palindrome-number/
def isPalindrome(x):
    str_x = str(x)
    rev_str_x = str_x[::-1]

    return str_x == rev_str_x


print(isPalindrome(-121))
