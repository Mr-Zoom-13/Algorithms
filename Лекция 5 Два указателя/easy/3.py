# https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/C

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

l = 0
r = 0
ans = 0
while l < n and r < m:
    if a[l] < b[r]:
        l += 1
    elif a[l] > b[r]:
        r += 1
    else:
        x, y = 0, 0
        while (l + x) < n and a[l + x] == a[l]:
            x += 1
        while (r + y) < m and b[r + y] == b[r]:
            y += 1
        l += x
        r += y
        ans += x * y

print(ans)
