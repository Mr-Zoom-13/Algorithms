# https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/E
from collections import defaultdict


class Segment:
    def __init__(self, k):
        self.dct = defaultdict(int)
        self.cur = 0
        self.k = k

    def add(self, elem):
        self.dct[elem] += 1
        if self.dct[elem] == 1:
            self.cur += 1

    def remove(self, elem):
        self.dct[elem] -= 1
        if self.dct[elem] == 0:
            self.cur -= 1

    def is_good(self):
        return self.cur <= self.k


n, s = map(int, input().split())
seg = Segment(s)
a = list(map(int, input().split()))
ans = 0
l = 0

for r in range(n):
    seg.add(a[r])

    while not seg.is_good():
        seg.remove(a[l])
        l += 1

    if seg.is_good():
        ans += r - l + 1

print(ans)
