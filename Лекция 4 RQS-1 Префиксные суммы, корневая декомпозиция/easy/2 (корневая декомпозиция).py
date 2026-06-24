import math

n = int(input())
a = list(map(int, input().split()))
q = int(input())
d = 1024 # n ** 0.5
blocks = [0] * math.ceil(n / d)

for _ in range(q):
    l, r, val = map(int, input().split())
    l -= 1
    r -= 1
    while l <= r:
        if l % d == 0 and l + d <= r:
            blocks[l // d] += val
            l += d
        else:
            a[l] += val
            l += 1

for i in range(n):
    print(a[i] + blocks[i // d], end=' ')
