# https://contest.yandex.ru/contest/45469/problems/11/


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


t = int(input())
for _ in range(t):
    arr = list(map(float, input().split()))
    n = int(arr[0])
    arr = arr[1:]


    res = []

    check_min = arr[::-1]
    minimums = []
    cur_min = 10000000000000000
    for i in range(n):
        cur_min = min(cur_min, check_min[i])
        minimums.append(cur_min)

    minimums = minimums[::-1]

    stack_storage = Stack()
    for i in range(n):
        if arr[i] != minimums[i]:
            while stack_storage.size() and arr[i] > stack_storage.back():
                res.append(stack_storage.pop())
            stack_storage.push(arr[i])
        else:
            while stack_storage.size() and arr[i] > stack_storage.back():
                res.append(stack_storage.pop())
            res.append(arr[i])
    while stack_storage.size():
        res.append(stack_storage.pop())
    if res == sorted(arr):
        print(1)
    else:
        print(0)
