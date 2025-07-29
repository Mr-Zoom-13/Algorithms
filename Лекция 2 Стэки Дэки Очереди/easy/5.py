# https://contest.yandex.ru/contest/45469/problems/17/

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


class Queue:
    def __init__(self):
        self.st1 = Stack()
        self.st2 = Stack()

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

    def push_center(self, n):
        cur_pos = (self.st1.size() + self.st2.size()) // 2
        if cur_pos >= self.st1.size():
            cur_pos -= self.st1.size()
            self.st2.arr.insert(cur_pos, n)
        else:
            self.st1.arr.insert(self.st1.size() - cur_pos, n)


queue = Queue()
n = int(input())
for i in range(n):
    cmd = input()
    if "+" in cmd:
        n = int(cmd.split()[1])
        queue.push(n)
    elif "*" in cmd:
        n = int(cmd.split()[1])
        queue.push_center(n)
    else:
        print(queue.pop())
