# https://codeforces.com/problemset/problem/1730/B

EPS = 10**(-7)

def binary_search(l, r, n, x, t):
    m_1 = l + (r - l) / 3
    m_2 = r - (r - l) / 3
    func_1 = func(m_1, n, x, t)
    func_2 = func(m_2, n, x, t)
    if func_1 > func_2:
        l = m_1
    else:
        r = m_2
    if (r - l) <= EPS:
        return r
    return binary_search(l, r, n, x, t)


def func(ans, n, x, t):

    cur_time = 0
    for i in range(n):
        cur_time = max(cur_time, t[i] + abs(ans - x[i]))

    return cur_time



T = int(input())
for _ in range(T):
    n = int(input())
    x = list(map(int, input().split()))
    t = list(map(int, input().split()))
    print(binary_search(-1, 10**10, n, x, t))

