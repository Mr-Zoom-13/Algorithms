# https://contest.yandex.ru/contest/45468/problems/20/


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



heap = MyHeap()
n = int(input())
arr = list(map(int, input().split()))
for i in arr:
    heap.insert(-i)
for i in range(n):
    print(-heap.extract(), end=" ")
