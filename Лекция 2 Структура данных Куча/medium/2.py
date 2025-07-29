# https://contest.yandex.ru/contest/45469/problems/19/


class MinHeap:
    def __init__(self):
        self.arr = []

    def insert(self, k):
        self.arr.append(k)
        cur_index = len(self.arr) - 1
        parent_index = (cur_index - 1 - (cur_index % 2 == 0)) // 2
        while parent_index >= 0 and self.arr[cur_index] < self.arr[parent_index]:
            self.arr[cur_index], self.arr[parent_index] = self.arr[parent_index], self.arr[cur_index]
            cur_index, parent_index = parent_index, (parent_index - 1 - (parent_index % 2 == 0)) // 2

    def get_min(self):
        if not self.arr:
            return (100000000**2, 0)
        return self.arr[0]

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
        if left_child < n and self.arr[cur_index] > self.arr[left_child]:
            cur_index = left_child
        if right_child < n and self.arr[cur_index] > self.arr[right_child]:
            cur_index = right_child

        if cur_elem != cur_index:
            self.arr[cur_elem], self.arr[cur_index] = self.arr[cur_index], self.arr[cur_elem]
            self.sift_down(cur_index, n)


heap = MinHeap()
n = int(input())
arr = input().split()
for i in arr:
    heap.insert(int(i))
ans = 0
while len(heap.arr) > 1:
    cur = heap.extract() + heap.extract()
    ans += cur * 0.05
    heap.insert(cur)
if len(str(round(ans, 2)).split(".")[1]) == 1:
    print(str(round(ans, 2)) + "0")
else:
    print(round(ans, 2))