# https://contest.yandex.ru/contest/45469/problems/18/


class MyHeap:
    def __init__(self):
        self.arr = []

    def insert(self, cur_arrive, cur_departure, number, k):
        self.arr.append((cur_arrive, number))
        cur_index = len(self.arr) - 1
        parent_index = (cur_index - 1 - (cur_index % 2 == 0)) // 2
        while parent_index >= 0 and self.arr[cur_index][0] > self.arr[parent_index][0]:
            self.arr[cur_index], self.arr[parent_index] = self.arr[parent_index], self.arr[cur_index]
            cur_index, parent_index = parent_index, (parent_index - 1 - (parent_index % 2 == 0)) // 2
        if parent_index >= 0:
            if self.arr[parent_index][0] == cur_arrive:
                if (self.arr[parent_index][2] + 1) > k:
                    print(f"0 {number}")
                    exit()
                else:
                    self.arr[cur_index] = (cur_departure, self.arr[cur_index][1], self.arr[parent_index][2] + 1)
            else:
                self.arr[cur_index] = (cur_departure, self.arr[cur_index][1], self.arr[parent_index][2])
        else:
            self.arr[cur_index] = (cur_departure, self.arr[cur_index][1], 1)

    def get_max(self):
        if not self.arr:
            return -10000
        return self.arr[0]

    # def extract(self):
    #     first = self.arr[0]
    #     self.arr[0] = self.arr[-1]
    #     del self.arr[-1]
    #     self.sift_down(0, len(self.arr))
    #     return first
    #
    #
    # def sift_down(self, cur_index, n):
    #     cur_elem = cur_index
    #     left_child = 2 * cur_index + 1
    #     right_child = 2 * cur_index + 2
    #     if left_child < n and self.arr[cur_index] < self.arr[left_child]:
    #         cur_index = left_child
    #     if right_child < n and self.arr[cur_index] < self.arr[right_child]:
    #         cur_index = right_child
    #
    #     if cur_elem != cur_index:
    #         self.arr[cur_elem], self.arr[cur_index] = self.arr[cur_index], self.arr[cur_elem]
    #         self.sift_down(cur_index, n)


k, n = map(int, input().split())
tupik = MyHeap()
for number in range(n):
    cur_arrive, cur_departure = map(int, input().split())
    tupik.insert(cur_arrive, cur_departure, number, k)
