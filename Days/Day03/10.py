s = input()
t = input()
def containsInT(substr, t):
    freqT = {} 
    for ch in t:
        freqT[ch] = freqT.get(ch, 0) + 1
    freqS = {}
    for ch in substr:
        freqS[ch] = freqS.get(ch,0) + 1
    for fr in freqT: 
        if fr not in freqS:
            return False 
        if freqT[fr] != freqS[fr]:
            return False 
    return True 

def minWinStr(s, t):    
    n = len(s)
    minStr = '*' * (n + 1)
    for I in range(n):
        for J in range(I,n):
            substr = s[I:J+1]
            if containsInT(substr, t):
                if len(substr) < len(minStr):
                    minStr = substr
    return minStr
print(minWinStr(s, t))