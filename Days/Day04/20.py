def doSort(nums):
    n = len(nums)
    for I in range(n-1):
        min_index = I 
        for J in range(I+1,n):
            if nums[J] < nums[min_index]:
                min_index =J
        if I != min_index:
            nums[I], nums[min_index] = nums[min_index], nums[I]
n = int(input())
nums = list(map(int, input().split()))[:n]
doSort(nums)
print(' '.join([str(e) for e in nums]))