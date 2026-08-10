# https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/G
import math


class Stack:
    def __init__(self):
        self.arr = []
        self.size = 0

    def push(self, elem):
        self.arr.append(elem)
        self.size += 1

    def top(self):
        return self.arr[-1]

    def pop(self):
        self.size -= 1
        return self.arr.pop()


class StackGCD:
    def __init__(self):
        self.simple_stack = Stack()
        self.gcd_stack = Stack()

    def push(self, elem):
        self.simple_stack.push(elem)
        if not self.gcd_stack.size:
            self.gcd_stack.push(elem)
        else:
            self.gcd_stack.push(math.gcd(elem, self.gcd_stack.top()))

    def top(self):
        return self.simple_stack.top()

    def pop(self):
        self.gcd_stack.pop()
        return self.simple_stack.pop()

    def size(self):
        return self.simple_stack.size

    def get_gcd(self):
        if self.gcd_stack.size:
            return self.gcd_stack.top()
        return 0


class Queue:
    def __init__(self):
        self.st1 = StackGCD()
        self.st2 = StackGCD()

    def push(self, elem):
        self.st1.push(elem)

    def top(self):
        if self.st2.size() == 0:
            while self.st1.size() > 0:
                self.st2.push(self.st1.pop())
        return self.st2.top()

    def pop(self):
        if self.st2.size() == 0:
            while self.st1.size() > 0:
                self.st2.push(self.st1.pop())
        return self.st2.pop()

    def get_gcd(self):
        return math.gcd(self.st1.get_gcd(), self.st2.get_gcd())


class Segment:
    def __init__(self):
        self.queue = Queue()

    def add(self, elem):
        self.queue.push(elem)

    def remove(self):
        self.queue.pop()

    def is_good(self):
        return self.queue.get_gcd() == 1


n = int(input())
seg = Segment()
a = list(map(int, input().split()))
l = 0
ans = 10**18

for r in range(n):
    seg.add(a[r])

    flag = seg.is_good()
    while seg.is_good():
        seg.remove()
        l += 1

    if flag:
        ans = min(ans, r - l + 2)
if ans == 10**18:
    print(-1)
else:
    print(ans)
