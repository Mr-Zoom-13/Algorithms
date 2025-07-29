# https://contest.yandex.ru/contest/45468/problems/12/

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


s = input()
flag = True
stack = Stack()

for i in s:
    if i in "([{":
        stack.push(i)
    else:
        elem = stack.pop()
        if i == ")":
            if elem == "{" or elem == "[" or elem == "error":
                print("no")
                flag = False
                break
        elif i == "]":
            if elem == "(" or elem == "{" or elem == "error":
                print("no")
                flag = False
                break
        elif i == "}":
            if elem == "(" or elem == "[" or elem == "error":
                print("no")
                flag = False
                break
if stack.size() != 0 and flag:
    print("no")
else:
    if flag:
        print('yes')
