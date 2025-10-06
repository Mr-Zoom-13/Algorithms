# https://codeforces.com/contest/1593/problem/C

# def binary_search(l, r, n, k, x):
#     m = l + (r - l) // 2
#
#     if func(m, n, k, x):
#         l = m
#     else:
#         r = m
#
#     if (r - l) == 1:
#         return r
#     return binary_search(l, r, n, k, x)
#
#
# def func(ans, n, k, x):
#     pass


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    x = sorted(list(map(int, input().split())))
    cur_x = 0
    ans = 0
    for i in range(k - 1, -1, -1):
        if x[i] > cur_x:
            cur_x += n - x[i]
            ans += 1
        else:
            break
    print(ans)


