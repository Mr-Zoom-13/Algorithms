# https://codeforces.com/edu/course/2/lesson/5/3/practice/contest/280799/problem/A

n, m = map(int, input().split())
tree = [0] * (4 * n)


def set_tree(start, value, l, r, q_l, q_r):
    global tree

    if q_l >= r or q_r < l:
        return

    if (r - l) == 1:
        tree[start] = value
        return
    m = (l + r) // 2
    set_tree(2 * start + 1, value, l, m, q_l, q_r)
    set_tree(2 * start + 2, value, m, r, q_l, q_r)
    tree[start] = tree[2 * start + 1] + tree[2 * start + 2]


def get_maximum(start):
    global tree

    if tree[start] > tree[2 * start + 1] and tree[start] > tree[2 * start + 2]:
        return tree[start]
    if tree[start] < tree[2 * start + 1] and tree[2 * start + 1] > tree[2 * start + 2]:
        return get_maximum(2 * start + 1)
    return get_maximum(2 * start + 1)


for _ in range(m):
    l, r, v = map(int, input().split())
    set_tree(0, v, 0, n, l, r - 1)
    print(get_maximum(0))