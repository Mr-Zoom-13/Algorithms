n = int(input())
a = list(map(int, input().split()))
q = int(input())

diff = [0] * (n + 1)

for _ in range(q):
    l, r, val = map(int, input().split())
    l -= 1
    diff[l] += val
    diff[r] -= val

current = 0
for i in range(n):
    current += diff[i]
    print(a[i] + current, end=' ')
