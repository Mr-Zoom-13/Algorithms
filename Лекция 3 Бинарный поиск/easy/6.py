# https://codeforces.com/edu/course/2/lesson/6/3/practice/contest/285083/problem/A

EPS = 10**(-6)

def binary_search(l, r):
    m = l + (r - l) / 2

    if func(m):
        r = m
    else:
        l = m

    if (r - l) <= EPS:
        return r
    return binary_search(l, r)


def func(ans):
    minimum = -10**9
    maximum = 10**9
    for human in people:
        minimum = max(minimum, human[0] - human[1] * ans)
        maximum = min(maximum, human[0] + human[1] * ans)
    if minimum <= maximum:
        return True
    return False



N = int(input())
people = []
for i in range(N):
    people.append(tuple(map(int, input().split())))

print(binary_search(-1, 10**9))