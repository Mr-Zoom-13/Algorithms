# https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F


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


class StackMinMax:
    def __init__(self):
        self.simple_stack = Stack()
        self.min_stack = Stack()
        self.max_stack = Stack()

    def push(self, elem):
        self.simple_stack.push(elem)
        if self.min_stack.size:
            self.min_stack.push(min(elem, self.min_stack.top()))
            self.max_stack.push(max(elem, self.max_stack.top()))
        else:
            self.min_stack.push(elem)
            self.max_stack.push(elem)

    def top(self):
        return self.simple_stack.top()

    def pop(self):
        self.min_stack.pop()
        self.max_stack.pop()
        return self.simple_stack.pop()

    def size(self):
        return self.simple_stack.size

    def get_minimum(self):
        if self.min_stack.size:
            return self.min_stack.top()
        return 10 ** 18

    def get_maximum(self):
        if self.max_stack.size:
            return self.max_stack.top()
        return -(10 ** 18)


class Queue:
    def __init__(self):
        self.st1 = StackMinMax()
        self.st2 = StackMinMax()

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

    def get_minimum(self):
        return min(self.st1.get_minimum(), self.st2.get_minimum())

    def get_maximum(self):
        return max(self.st1.get_maximum(), self.st2.get_maximum())


class Segment:
    def __init__(self, k):
        self.queue = Queue()
        self.k = k

    def add(self, elem):
        self.queue.push(elem)

    def remove(self):
        self.queue.pop()

    def is_good(self):
        minimum = self.queue.get_minimum()
        maximum = self.queue.get_maximum()
        return (maximum - minimum) <= self.k


n, k = map(int, input().split())
seg = Segment(k)
a = list(map(int, input().split()))
l = 0
ans = 0

for r in range(n):
    seg.add(a[r])

    while not seg.is_good():
        seg.remove()
        l += 1

    if seg.is_good():
        ans += r - l + 1
print(ans)
