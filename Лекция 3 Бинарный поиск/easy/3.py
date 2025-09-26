# https://informatics.msk.ru/mod/statements/view.php?id=1966&chapterid=1620#1


def binary_search(l, r):
    m = l + (r - l) // 2
    if func(m):
        r = m
    else:
        l = m
    if r - l == 1:
        return r
    return binary_search(l, r)


def func(ans):
    # Текущий неиспользованный ученик
    i = 0
    # Текущее кол-во бригад
    r = 0

    while r != R and i != N and (i + C - 1) < N:
        if (students[i + C - 1] - students[i]) <= ans:
            r += 1
            i = i + C
        else:
            i += 1
    if r == R:
        return True
    return False



N, R, C = [int(i) for i in input().split()]
students = []
for i in range(N):
    students.append(int(input()))
students.sort()

print(binary_search(-1, 10**9 + 1))

