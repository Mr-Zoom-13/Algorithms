# https://codeforces.com/edu/course/2/lesson/5/3/practice/contest/280799/problem/A
import random


class Node:
    def __init__(self):
        self.max_sum = 0
        self.sum = 0
        self.pref_sum = 0
        self.suf_sum = 0

    def __repr__(self):
        return f"max_sum: {self.max_sum} pref: {self.pref_sum} suf: {self.suf_sum}"



def set_tree(tree, start, value, l, r, q_l, q_r):
    if q_l >= r or q_r < l:
        return

    if (r - l) == 1:
        tree[start].max_sum = value
        tree[start].sum = value
        tree[start].pref_sum = value
        tree[start].suf_sum = value
        return
    m = (l + r) // 2
    set_tree(tree, 2 * start + 1, value, l, m, q_l, q_r)
    set_tree(tree, 2 * start + 2, value, m, r, q_l, q_r)


    tree[start].max_sum = max(tree[2 * start + 1].max_sum, tree[2 * start + 2].max_sum, tree[2 * start + 1].suf_sum + tree[2 * start + 2].pref_sum)
    tree[start].sum = tree[2 * start + 1].sum + tree[2 * start + 2].sum

    # if (m - l) == 1:
    #     tree[start].pref_sum = max(tree[2 * start + 1].pref_sum, tree[2 * start + 1].pref_sum + tree[2 * start + 2].pref_sum)
    # else:
    #     tree[start].pref_sum = max(tree[2 * start + 1].pref_sum, tree[2 * start + 1].pref_sum + tree[2 * start + 1].suf_sum)
    #
    # if (r - m) == 1:
    #     tree[start].suf_sum = max(tree[2 * start + 2].suf_sum, tree[2 * start + 1].suf_sum + tree[2 * start + 2].pref_sum)
    # else:
    #     tree[start].suf_sum = max(tree[2 * start + 2].suf_sum, tree[2 * start + 1].suf_sum + tree[2 * start + 2].pref_sum + tree[2 * start + 2].suf_sum)


    tree[start].pref_sum = max(tree[2 * start + 1].pref_sum, tree[2 * start + 1].sum + tree[2 * start + 2].pref_sum)
    tree[start].suf_sum = max(tree[2 * start + 2].suf_sum, tree[2 * start + 2].sum + tree[2 * start + 1].suf_sum)


# def get_maximum(tree, start):
#     if tree[start].max_sum >= tree[2 * start + 1].max_sum and tree[start].max_sum >= tree[2 * start + 2].max_sum:
#         return tree[start].max_sum
#     if tree[start].max_sum < tree[2 * start + 1].max_sum and tree[2 * start + 1].max_sum > tree[2 * start + 2].max_sum:
#         return get_maximum(tree, 2 * start + 1)
#     return get_maximum(tree, 2 * start + 2)



def ideal_command(tree, n, l, r, v):
    set_tree(tree, 0, v, 0, n, l, r - 1)
    answer = tree[0].max_sum
    if answer < 0:
        return 0
    return answer



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
#             tree = []
#             for _ in range(4 * n):
#                 tree.append(Node())
#             commands = []
#             for _ in range(m):
#                 l = random.randint(0, n - 1)
#                 r = random.randint(l + 1, n)
#                 v = random.randint(-10, 10)
#                 commands.append(f"{l} {r} {v}")
#                 stupid_answer = stupid_command(stupid_lst, n, l, r, v)
#                 try:
#                     ideal_answer = ideal_command(tree, n, l, r, v)
#                     assert stupid_answer == ideal_answer, f"{n}, {m}, {commands}, {stupid_answer}, {ideal_answer}"
#                 except Exception as e:
#                     print(e)
#                     print(f"{n}, {m}, {commands}, {stupid_answer}")
#                     exit()
#
#
# generate_samples()

def print_tree(tree):
    print("-" * 100)
    for i in range(len(tree)):
        print(f"{i}. {tree[i]}")
    print("-" * 100)

n, m = map(int, input().split())
tree = []
for _ in range(4 * n):
    tree.append(Node())
for _ in range(m):
    l, r, v = map(int, input().split())
    print(ideal_command(tree, n, l, r, v))
