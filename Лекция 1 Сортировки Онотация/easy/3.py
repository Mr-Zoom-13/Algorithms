nums = [0, 1, 2, 0, 0, 2]
counter = [0, 0, 0]
for i in range(len(nums)):
    counter[nums[i]] += 1
for i in range(len(nums)):
    if i < counter[0]:
        nums[i] = 0
    elif i - counter[0] < counter[1]:
        nums[i] = 1
    else:
        nums[i] = 2
print(nums)