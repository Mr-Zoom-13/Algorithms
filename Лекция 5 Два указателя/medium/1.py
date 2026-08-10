# https://codeforces.com/edu/course/2/lesson/9/3/practice/contest/307094/problem/B

class Segment():
    def __init__(self, s):
        self.cur = 0
        self.s = s

    def push(self, elem):
        self.cur += elem

    def remove(self, elem):
        self.cur -= elem

    def is_good(self):
        return self.cur <= self.s



n, s = map(int, input().split())
seg = Segment(s)
a = list(map(int, input().split()))
ans = 0
l = 0

for r in range(n):
    seg.push(a[r])

    while not seg.is_good():
        seg.remove(a[l])
        l += 1
    dlina = r - l + 1
    ans += int((1 + dlina) / 2 * dlina)

print(ans)
