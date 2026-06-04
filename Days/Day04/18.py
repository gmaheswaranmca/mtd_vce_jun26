def search(nums, key):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid1 = left + ((right - left) // 3)
        mid2 = right - ((right - left) // 3)
        if nums[mid1] == key:
            return mid1
        elif nums[mid2] == key:
            return mid2
        elif key < nums[mid1]:
            right = mid1 - 1
        elif key > nums[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    return -1
n = int(input())
nums = list(map(int, input().split()))[:n]
key = int(input())
print(search(nums, key))