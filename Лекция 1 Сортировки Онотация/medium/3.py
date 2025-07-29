# https://codeforces.com/problemset/problem/1713/B


t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    flag = True
    max_element = max(nums)
    ind_max = nums.index(max_element)

    # Проверяем что все числа до максимального возрастают
    for i in range(ind_max):
        if nums[i] > nums[i + 1]:
            flag = False
            break

    # Проверяем что все числа после максимального убывают
    for i in range(ind_max, len(nums) - 1):
        if nums[i] < nums[i + 1]:
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")
