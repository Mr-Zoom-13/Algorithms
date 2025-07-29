# https://leetcode.com/problems/top-k-frequent-elements/description/
from collections import defaultdict

nums = [1,1,1,2,2,3]
k = 2

counter = defaultdict(int)
# for i in range(-10000, 10001):
#     counter[i] = 0

for i in range(len(nums)):
    counter[nums[i]] += 1

check = []
for item in counter.items():
    check.append((item[1], item[0]))
check.sort(reverse=True)

res = []
for i in range(k):
    res.append(check[i][1])
print(res)