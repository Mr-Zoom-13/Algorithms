# https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/D


class Segment:
    def __init__(self, s):
        self.cur = 0
        self.s = s

    def add(self, elem):
        self.cur += elem

    def remove(self, elem):
        self.cur -= elem

    def is_good(self):
        return self.cur >= self.s

    def still_good_after_removal(self, elem):
        return (self.cur - elem) >= self.s


n, s = map(int, input().split())
seg = Segment(s)
a = list(map(int, input().split()))
ans = 0
l = 0

for r in range(n):
    seg.add(a[r])

    while seg.still_good_after_removal(a[l]):
        seg.remove(a[l])
        l += 1

    if seg.is_good():
        ans += l + 1

print(ans)
