# https://codeforces.com/edu/course/2/lesson/5/3/practice/contest/280799/problem/A
import random


class Node:
    def __init__(self):
        self.max_sum = 0
        self.max_near_sum = 0



def set_tree(tree, start, value, l, r, q_l, q_r):
    if q_l >= r or q_r < l:
        return

    if (r - l) == 1:
        tree[start].max_sum = value
        tree[start].max_near_sum = value
        return
    m = (l + r) // 2
    set_tree(tree, 2 * start + 1, value, l, m, q_l, q_r)
    set_tree(tree, 2 * start + 2, value, m, r, q_l, q_r)

    tree[start].max_sum = max(tree[2 * start + 1].max_sum, tree[2 * start + 2].max_sum, tree[2 * start + 1].max_near_sum + tree[2 * start + 2].max_near_sum)

    tree[start] = tree[2 * start + 1] + tree[2 * start + 2]


def get_maximum(tree, start):
    if tree[start] >= tree[2 * start + 1] and tree[start] >= tree[2 * start + 2]:
        return tree[start]
    if tree[start] < tree[2 * start + 1] and tree[2 * start + 1] > tree[2 * start + 2]:
        return get_maximum(tree, 2 * start + 1)
    return get_maximum(tree, 2 * start + 2)



def ideal_command(tree, n, l, r, v):
    set_tree(tree, 0, v, 0, n, l, r - 1)
    return get_maximum(tree, 0)



def stupid_command(stupid_lst, n, l, r, v):
    for i in range(l, r):
        stupid_lst[i] = v
    maximum = 0
    for i in range(0, n):
        s = stupid_lst[i]
        maximum = max(maximum, s)
        for j in range(i + 1, n):
            s += stupid_lst[j]
            maximum = max(maximum, s)
    return maximum



# def generate_samples():
#     for n in range(1, 100):
#         for m in range(1, 100):
#             stupid_lst = [0] * n
#             tree = [0] * (100 * n)
#             commands = []
#             for _ in range(m):
#                 l = random.randint(0, n - 1)
#                 r = random.randint(l + 1, n)
#                 v = random.randint(-10, 10)
#                 commands.append(f"{l} {r} {v}")
#                 stupid_answer = stupid_command(stupid_lst, n, l, r, v)
#                 ideal_answer = ideal_command(tree, n, l, r, v)
#                 assert stupid_answer == ideal_answer, f"{n}, {m}, {commands}, {stupid_answer}, {ideal_answer}"
#
#
# generate_samples()


n, m = map(int, input().split())
tree = [Node()] * (4 * n)
for _ in range(m):
    l, r, v = map(int, input().split())
    print(ideal_command(tree, n, l, r, v))
