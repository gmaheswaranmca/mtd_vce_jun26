def search(nums, key):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + ((right - left) // 2)
        if nums[mid] == key:
            return mid
        elif key < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1
n = int(input())
nums = [int(e) for e in input().split(' ')][:n]
key = int(input())
print(search(nums, key))
