n, q = map(int, input().split())
a = [int(i) for i in input().split()]
pref = [0]
for i in range(n):
    pref.append(pref[-1] + a[i])
for _ in range(q):
    l, r = map(int, input().split())
    print(pref[r] - pref[l])


