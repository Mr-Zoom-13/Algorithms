# https://contest.yandex.ru/contest/45468/problems/19/
import random
from heapq import heapify
from math import log2


class MyHeap:
    def __init__(self):
        self.arr = []

    def insert(self, k):
        self.arr.append(k)
        cur_index = len(self.arr) - 1
        parent_index = (cur_index - 1 - (cur_index % 2 == 0)) // 2
        while parent_index >= 0 and self.arr[cur_index] > self.arr[parent_index]:
            self.arr[cur_index], self.arr[parent_index] = self.arr[parent_index], self.arr[cur_index]
            cur_index, parent_index = parent_index, (parent_index - 1 - (parent_index % 2 == 0)) // 2

    def extract(self):
        first = self.arr[0]
        self.arr[0] = self.arr[-1]
        del self.arr[-1]
        self.sift_down(0, len(self.arr))
        return first


    def sift_down(self, cur_index, n):
        cur_elem = cur_index
        left_child = 2 * cur_index + 1
        right_child = 2 * cur_index + 2
        if left_child < n and self.arr[cur_index] < self.arr[left_child]:
            cur_index = left_child
        if right_child < n and self.arr[cur_index] < self.arr[right_child]:
            cur_index = right_child

        if cur_elem != cur_index:
            self.arr[cur_elem], self.arr[cur_index] = self.arr[cur_index], self.arr[cur_elem]
            self.sift_down(cur_index, n)

    def heapify(self):
        pass


# testi = [7, 8, 3, 10, 7, 2, 3, 1, 4, 5]
# heap = MyHeap()
# heap.arr = testi
# heap.heapify()
# print(heap.arr)

# for i in range(100):
#     lst1 = [random.randint(1, 10) for j in range(10)]
#     ready_system = [-j for j in lst1]
#     heapify(ready_system)
#     ready_system = [-j for j in ready_system]
#     heap = MyHeap()
#     heap.arr = lst1
#     heap.heapify()
#     if ready_system != heap.arr:
#         print(lst1, ready_system, heap.arr)

heap = MyHeap()
n = int(input())
for i in range(n):
    cmd = input().split()
    if cmd[0] == "0":
        heap.insert(int(cmd[1]))
    else:
        print(heap.extract())
