# https://informatics.msk.ru/mod/statements/view3.php?chapterid=756#1

class Stack:
    def __init__(self):
        self.arr = []

    def push(self, n):
        self.arr.append(n)
        return "ok"

    def pop(self):
        return self.arr.pop() if self.size() else "error"

    def back(self):
        return self.arr[-1] if self.size() else "error"

    def size(self):
        return len(self.arr)

    def clear(self):
        self.arr = []
        return "ok"


class MinStack:
    def __init__(self):
        self.stack = Stack()
        self.min_stack = Stack()

    def push(self, n):
        self.stack.push(n)
        if self.min_stack.size():
            minimum = min(self.min_stack.back(), n)
        else:
            minimum = n
        return self.min_stack.push(minimum)

    def pop(self):
        self.min_stack.pop()
        return self.stack.pop()

    def back(self):
        return self.stack.back()

    def size(self):
        return self.stack.size()

    def clear(self):
        self.min_stack.clear()
        return self.stack.clear()

    def get_min(self):
        return self.min_stack.back()


class Queue:
    def __init__(self):
        self.st1 = MinStack()
        self.st2 = MinStack()

    def push(self, n):
        return self.st1.push(n)

    def pop(self):
        if not self.st2.size():
            while self.st1.size():
                self.st2.push(self.st1.pop())
        return self.st2.pop()

    def front(self):
        if not self.st2.size():
            if self.st1.size():
                return self.st1.arr[0]
            return "error"
        return self.st2.back()

    def size(self):
        return self.st2.size() + self.st1.size()

    def clear(self):
        self.st1.clear()
        return self.st2.clear()

    def get_min(self):
        if not self.st2.size():
            return self.st1.get_min()
        return min(self.st1.get_min(), self.st2.get_min())


queue = Queue()
n, k = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(k):
    queue.push(arr[i])
print(queue.get_min())
for i in range(k, n):
    queue.pop()
    queue.push(arr[i])
    print(queue.get_min())
