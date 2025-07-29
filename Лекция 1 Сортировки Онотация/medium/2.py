# https://leetcode.com/problems/wiggle-sort-ii/description/

nums = [1,3,2,2,3,1]

counter = [0] * 5001
for i in range(len(nums)):
    counter[nums[i]] += 1

j = 1
for i in range(5000, -1, -1):
    while counter[i] != 0:
        if j >= len(nums):
            j = 0
        nums[j] = i
        j += 2
        counter[i] -= 1
print(nums)