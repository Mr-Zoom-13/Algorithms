# https://contest.yandex.ru/contest/45468/problems/15/


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


class MonotonicStack:
    def __init__(self, n):
        self.st = Stack()
        self.res = ['-1'] * n

    def push(self, n, pos):
        while self.st.back() != "error" and n < self.st.back()[0]:
            st_n, st_pos = self.st.pop()
            self.res[st_pos] = str(pos)
        self.st.push((n, pos))



n = int(input())
arr = list(map(int, input().split()))
stack = MonotonicStack(n)
for i in range(n):
    stack.push(arr[i], i)
print(" ".join(stack.res))