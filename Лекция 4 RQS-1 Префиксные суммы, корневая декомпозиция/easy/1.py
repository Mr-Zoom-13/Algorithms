f = open("sum2.in", "r")
res = open("sum2.out", "w")
n = int(f.readline())
a = [int(i) for i in f.readline().split()]
pref = [0]
for i in range(n):
    pref.append(pref[-1] + a[i])
m = int(f.readline())
for _ in range(m):
    l, r = map(int, f.readline().split())
    res.write(str(pref[r] - pref[l - 1]) + "\n")
f.close()
res.close()

