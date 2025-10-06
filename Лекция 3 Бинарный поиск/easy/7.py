# https://codeforces.com/edu/course/2/lesson/6/3/practice/contest/285083/problem/B


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
    if max(arr) > ans:
        return False

    i = 0
    cur_sum = 0
    k = 1

    while i != N:
        if (cur_sum + arr[i]) <= ans:
            cur_sum += arr[i]
        else:
            cur_sum = arr[i]
            k += 1
        i += 1

    if k <= K:
        return True
    return False

N, K = map(int, input().split())
arr = list(map(int, input().split()))

print(binary_search(0, 10**20))

# 3 2
# 100 1 1