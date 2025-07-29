# https://contest.yandex.ru/contest/45469/problems/14/
from random import randint


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



def ne(arr):
    n = len(arr)
    answer = [0]*n
    for i in range(n):
        counter = 0
        # Влево смотрим
        for j in range(i, -1, -1):
            if arr[j] < arr[i]:
                break
            counter += 1

        # Вправо смотрим
        for j in range(i, n):
            if arr[j] < arr[i]:
                break
            counter += 1
        answer[i] = (counter - 1) * arr[i]
    return answer


stack = Stack()
arr = list(map(int, input().split()))
n = arr[0]
arr = arr[1:]
# Список ответов (площадь i-го прямоугольника если его максимально расширить влево и вправо
ans = [0]*n

# Как задача 1. Пытаемся расширить прямоугольник максимально вправо
for i in range(n):
    while stack.size() and arr[i] < stack.back()[0]:
        st_n, st_pos = stack.pop()
        ans[st_pos] += (i - st_pos) * st_n
    stack.push((arr[i], i))

# Есть те, которые никогда не оборвались, дозаполняем их
i = n
while stack.size():
    st_n, st_pos = stack.pop()
    ans[st_pos] += (i - st_pos) * st_n
stack.clear()
# Как задача 1. Пытаемся расширить прямоугольник максимально влево
for i in range(n - 1, -1, -1):
    while stack.size() and arr[i] < stack.back()[0]:
        st_n, st_pos = stack.pop()
        ans[st_pos] += (st_pos - i - 1) * st_n
    stack.push((arr[i], i))

# Есть те, которые никогда не оборвались, дозаполняем их
i = -1
while stack.size():
    st_n, st_pos = stack.pop()
    ans[st_pos] += (st_pos - i - 1) * st_n

if len(ans) > 0:
    print(max(ans))
else:
    print(0)
