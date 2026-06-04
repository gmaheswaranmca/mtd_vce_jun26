def search(nums, key):
    for index, num in enumerate(nums):
        if num == key:
            return index
    return -1
n = int(input())
nums = [int(e) for e in input().split(' ')][:n]
key = int(input())
print(search(nums, key))