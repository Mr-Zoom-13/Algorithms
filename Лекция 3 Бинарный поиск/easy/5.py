# https://informatics.msk.ru/mod/statements/view.php?id=1966&chapterid=490#1

def binary_search(l, r):
    m = l + (r - l) // 2

    if func(m):
        r = m
    else:
        l = m
    if (r - l) == 1:
        return r
    return binary_search(l, r)


def func(ans):
    if ans == 4:
        pass
    ost = ans - min(x, y)
    n = ost // x + ost // y + 1
    if n >= N:
        return True
    return False


N, x, y = map(int, input().split())
print(binary_search(-1, 10 ** 9))
