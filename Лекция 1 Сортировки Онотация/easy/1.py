# https://codeforces.com/group/dAhOSPf3oD/contest/349149/problem/A


def merge(a, l, m, r):
    L = []
    for i in range(l, m + 1):
        L.append(a[i])

    R = []
    for i in range(m + 1, r + 1):
        R.append(a[i])

    i = 0
    j = 0
    k = l
    while i < (m + 1 - l) and j < (r - m):
        if L[i] < R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1

    while i < (m + 1 - l):
        a[k] = L[i]
        i += 1
        k += 1

    while j < (r - m):
        a[k] = R[j]
        j += 1
        k += 1


def merge_sort(a, l, r):
    if l == r:
        return
    m = l + (r - l) // 2
    merge_sort(a, l, m)
    merge_sort(a, m + 1, r)
    merge(a, l, m, r)


n = int(input())
a = list(map(int, input().split()))
merge_sort(a, 0, len(a) - 1)
print(' '.join(map(str, a)))
