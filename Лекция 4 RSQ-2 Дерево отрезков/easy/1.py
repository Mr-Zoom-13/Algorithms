# https://codeforces.com/edu/course/2/lesson/4/1/practice/contest/273169/problem/A

n, m = map(int, input().split())
lst = list(map(int, input().split()))
tree = [0] * (4 * n)

# Собираем дерево
def build_tree(start, l, r):
    global tree

    if (r - l) == 1:
        tree[start] = lst[l]
        return

    m = (l + r) // 2
    build_tree(2 * start + 1, l, m)
    build_tree(2 * start + 2, m, r)

    tree[start] = tree[2 * start + 1] + tree[2 * start + 2]


def set_tree(start, value, l, r, q_l, q_r):
    global tree

    if (r - l) == 1:
        if q_l == l:
            tree[start] = value
        return
    m = (l + r) // 2
    set_tree(2 * start + 1, value, l, m, q_l, q_r)
    set_tree(2 * start + 2, value, m, r, q_l, q_r)
    tree[start] = tree[2 * start + 1] + tree[2 * start + 2]


def get_sum(start, l, r, q_l, q_r):
    global tree

    if q_l >= r or q_r < l:
        return 0

    if (r - l) == 1:
        return tree[start]

    m = (l + r) // 2
    return get_sum(2 * start + 1, l, m, q_l, q_r) + get_sum(2 * start + 2, m, r, q_l, q_r)


build_tree(0, 0, n)

# Обработка запросов
for _ in range(m):
    command, q_l, q_r = map(int, input().split())
    if command == 1:
        set_tree(0, q_r, 0, n, q_l, q_l + 1)
    elif command == 2:
        print(get_sum(0, 0, n, q_l, q_r - 1))

