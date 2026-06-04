def findPairs(nums, k):
    visited = set()
    pairs = []
    for num in nums:
        complement = k - num 
        if complement in visited: 
            pair = tuple(sorted((complement, num)))
            if pair not in pairs:
                pairs.append(pair)
        visited.add(num)
    return list(sorted(pairs))

nums = [int(num_str) for num_str in input().split(',')]
k = int(input())
pairs = findPairs(nums, k)
for pair in pairs:
    print(pair)