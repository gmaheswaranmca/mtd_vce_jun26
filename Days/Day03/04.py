str = input()
def allCharsUnique(str):
    visited = set()
    for ch in str:
        if ch in visited:
            return False 
        visited.add(ch)
    return True 

def longestUniqueStr(s):
    maxLen = 0
    n = len(s)
    for I in range(n):
        for J in range(I,n):
            substr = s[I:J+1]
            if allCharsUnique(substr):
                maxLen = max(len(substr), maxLen)
    return maxLen 
print(longestUniqueStr(str))