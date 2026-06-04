def doSort(nums):
    n = len(nums)
    swapped = True 
    while swapped:
        swapped = False 
        for I in range(0,n-1):
            if nums[I] > nums[I+1]:
                nums[I], nums[I+1] = nums[I+1], nums[I] # swap
                swapped = True
n = int(input())
nums = list(map(int, input().split()))[:n]
doSort(nums)
print(' '.join([str(e) for e in nums]))