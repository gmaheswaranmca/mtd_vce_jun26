def doReversal(ids):
    left, right = 0, len(ids) - 1
    while left < right:
        ids[left], ids[right] = ids[right], ids[left]
        left += 1
        right -= 1
    
n = int(input())
ids = [int(id_str) for id_str in input().split(' ')]
doReversal(ids)
print(' '.join([str(id) for id in ids]))