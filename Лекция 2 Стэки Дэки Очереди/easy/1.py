# https://contest.yandex.ru/contest/45468/problems/11/

class Stack():
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


stack = Stack()
while True:
    cmd = input()
    if cmd == "pop":
        print(stack.pop())
    elif cmd == "back":
        print(stack.back())
    elif cmd == "size":
        print(stack.size())
    elif cmd == "clear":
        print(stack.clear())
    elif cmd == "exit":
        print("bye")
        break
    else:
        n = int(cmd.split()[1])
        print(stack.push(n))