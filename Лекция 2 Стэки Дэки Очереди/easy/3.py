# https://contest.yandex.ru/contest/45468/problems/16/


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


queue = Queue()
while True:
    cmd = input()
    if cmd == "pop":
        print(queue.pop())
    elif cmd == "front":
        print(queue.front())
    elif cmd == "size":
        print(queue.size())
    elif cmd == "clear":
        print(queue.clear())
    elif cmd == "exit":
        print("bye")
        break
    else:
        n = int(cmd.split()[1])
        print(queue.push(n))
