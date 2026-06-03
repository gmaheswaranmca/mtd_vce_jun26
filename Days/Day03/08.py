str = input()
def isPalindrome(str):
    n = len(str)
    left = 0
    right = n - 1
    while left < right:
        if str[left] != str[right]:
            return False 
        left += 1
        right -= 1
    return True 

def longestPalindrome(s):
    longest = ''
    n = len(s)
    for I in range(n):
        for J in range(I,n):
            substr = s[I:J+1]
            if isPalindrome(substr):
                if len(substr) > len(longest):
                    longest = substr
    return longest
print(longestPalindrome(str))