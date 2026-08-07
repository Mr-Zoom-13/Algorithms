# https://informatics.msk.ru/mod/statements/view.php?id=43201&chapterid=1663#1

n, k = map(int, input().split())
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

    tree[start] = min(tree[2 * start + 1], tree[2 * start + 2])


def set_tree(start, value, l, r, q_l, q_r):
    global tree

    if (r - l) == 1:
        if q_l == l:
            tree[start] = value
        return
    m = (l + r) // 2
    set_tree(2 * start + 1, value, l, m, q_l, q_r)
    set_tree(2 * start + 2, value, m, r, q_l, q_r)
    tree[start] = min(tree[2 * start + 1], tree[2 * start + 2])


def get_min(start, l, r, q_l, q_r):
    global tree

    if q_l >= r or q_r < l:
        return 10**9

    if (r - l) == 1:
        return tree[start]

    m = (l + r) // 2
    return min(get_min(2 * start + 1, l, m, q_l, q_r), get_min(2 * start + 2, m, r, q_l, q_r))


build_tree(0, 0, n)

start = 0
stop = k - 1
while stop < n:
    print(get_min(0, 0, n, start, stop), end=" ")
    start += 1
    stop += 1

