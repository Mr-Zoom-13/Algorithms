# https://codeforces.com/group/dAhOSPf3oD/contest/349149/problem/B

counter = [0] * 101

n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    counter[a[i]] += 1

text = ""
for i in range(101):
    text += (str(i) + " ") * counter[i]
print(text)
