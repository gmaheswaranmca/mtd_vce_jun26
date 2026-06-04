def containsSeq(S, T):
    I = 0
    J = 0
    n = len(S)
    m = len(T)
    while I < n and J < m:
        if S[I] == T[J]:
            J += 1
        I += 1
    return m == J
S = input()
T = input()
print('Yes' if containsSeq(S,T) else 'No')