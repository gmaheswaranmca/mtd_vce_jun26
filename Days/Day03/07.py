n = int(input())
nums = [int(num_str) for num_str in input().split(' ')][:n]
def maxSubArr(nums):
    n = len(nums)
    maxSum = float('-inf')
    for I in range(n):
        for J in range(I, n):
            s = 0
            for K in range(I, J + 1):
                s += nums[K]
            maxSum = max(s, maxSum)
    return maxSum 
print(maxSubArr(nums))