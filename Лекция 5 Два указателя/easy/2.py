# https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

l = 0
r = 0
while l < n and r < m:
    if a[l] < b[r]:
        l += 1
    else:
        print(l, end=" ")
        ans = 0
        r += 1

while r < m:
    print(n, end=" ")
    r += 1
