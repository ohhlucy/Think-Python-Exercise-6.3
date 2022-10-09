# function which return reverse of a string

def first(civic):
    return civic[0]


def last(civic):
    return civic[-1]


def middle(civic):
    return civic[1:-1]

def isPalindrome(s):
    return s == s[::-1]


# Check to see if word is a palindrome
s = "civic"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")





