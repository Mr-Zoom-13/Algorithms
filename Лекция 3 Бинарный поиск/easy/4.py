# https://informatics.msk.ru/mod/statements/view.php?id=1966&chapterid=1#1


def binary_search(l, r):
    m = l + (r - l) // 2
    if func(m):
        l = m
    else:
        r = m
    if (r - l) == 1:
        return l
    return binary_search(l, r)


def func(ans):
    # Текущее стойло
    i = 0
    # Текущее рассматриваемое стойло
    j = 1
    # Сколько коров в стойле уже
    k = 1

    while i != N and j != N and k != K:
        if (a[j] - a[i]) < ans:
            j += 1
        else:
            i = j
            j += 1
            k += 1
    if k == K:
        return True
    return False


N, K = map(int, input().split())
a = [int(i) for i in input().split()]
print(binary_search(0, 10**9))
