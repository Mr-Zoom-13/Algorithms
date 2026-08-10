# https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []

l = 0
r = 0

while l < n and r < m:
    if a[l] < b[r]:
        c.append(a[l])
        l += 1
    else:
        c.append(b[r])
        r += 1

while l < n:
    c.append(a[l])
    l += 1

while r < m:
    c.append(b[r])
    r += 1

print(*c, sep=" ")