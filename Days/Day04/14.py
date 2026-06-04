def collectWater(heights):
    n = len(heights)
    leftMax = [0] * n
    rightMax = [0] * n

    leftMax[0] = heights[0]
    for I in range(1, n):
        leftMax[I] = max(leftMax[I-1], heights[I])

    rightMax[n-1] = heights[n-1]
    for I in range(n-2, -1, -1):
        rightMax[I] = max(rightMax[I+1], heights[I])

    water = 0
    for I in range(n): 
        water += min(leftMax[I], rightMax[I]) - heights[I]
    return water 
n = int(input())
heights = [int(h_str) for h_str in input().split(' ')][:n]
print(collectWater(heights))