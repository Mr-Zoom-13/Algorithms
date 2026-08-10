# https://codeforces.com/edu/course/2/lesson/9/3/practice/contest/307094/problem/D
import random

ans = 10 ** 18
ans_x = -1
ans_y = -1
ans_z = -1
ans_u = -1

def solve_effective(n_1, n_2, n_3, n_4, a, b, c, d):
    global ans, ans_x, ans_y, ans_z, ans_u
    ans = 10 ** 18
    ans_x = -1
    ans_y = -1
    ans_z = -1
    ans_u = -1

    x = 0
    y = 0
    z = 0
    u = 0


    def recalc_ans(x, y, z, u):
        global ans, ans_x, ans_y, ans_z, ans_u
        maximum = max(a[x], b[y], c[z], d[u])
        minimum = min(a[x], b[y], c[z], d[u])
        new_ans = maximum - minimum
        if new_ans < ans:
            ans = new_ans
            ans_x = x
            ans_y = y
            ans_z = z
            ans_u = u


    while x < n_1 and y < n_2 and z < n_3 and u < n_4:
        recalc_ans(x, y, z, u)
        if a[x] <= b[y] and a[x] <= c[z] and a[x] <= d[u]:
            x += 1
        elif b[y] <= a[x] and b[y] <= c[z] and b[y] <= d[u]:
            y += 1
        elif c[z] <= a[x] and c[z] <= b[y] and c[z] <= d[u]:
            z += 1
        else:
            u += 1

    # return ans
    return [a[ans_x], b[ans_y], c[ans_z], d[ans_u]]



def solve_uneffective(n_1, n_2, n_3, n_4, a, b, c, d):
    ans = 10**18
    for i in range(n_1):
        for j in range(n_2):
            for k in range(n_3):
                for l in range(n_4):
                    minimum = min(a[i], b[j], c[k], d[l])
                    maximum = max(a[i], b[j], c[k], d[l])
                    ans = min(ans, maximum - minimum)
    return ans


def test():
    for _ in range(100000):
        n_1 = random.randint(1, 10)
        n_2 = random.randint(1, 10)
        n_3 = random.randint(1, 10)
        n_4 = random.randint(1, 10)
        a = [random.randint(1, 10)]
        for __ in range(n_1 - 1):
            a.append(random.randint(a[-1], a[-1] + 10))
        
        b = [random.randint(1, 10)]
        for __ in range(n_2 - 1):
            b.append(random.randint(b[-1], b[-1] + 10))
        
        c = [random.randint(1, 10)]
        for __ in range(n_3 - 1):
            c.append(random.randint(c[-1], c[-1] + 10))
        
        d = [random.randint(1, 10)]
        for __ in range(n_4 - 1):
            d.append(random.randint(d[-1], d[-1] + 10))


        ans_effective = solve_effective(n_1, n_2, n_3, n_4, a, b, c, d)
        ans_ineffective = solve_uneffective(n_1, n_2, n_3, n_4, a, b, c, d)
        assert ans_effective == ans_ineffective, f"{n_1}, {n_2}, {n_3}, {n_4}, {a}, {b}, {c}, {d}, {ans_effective}, {ans_ineffective}"

# AssertionError: 3, 1, 3, 2, [10, 16, 17], [10], [5, 5, 15], [1, 11], 2, 5
# test()

n_1 = int(input())
a = list(map(int, input().split()))
n_2 = int(input())
b = list(map(int, input().split()))
n_3 = int(input())
c = list(map(int, input().split()))
n_4 = int(input())
d = list(map(int, input().split()))
a.sort()
b.sort()
c.sort()
d.sort()
print(*solve_effective(n_1, n_2, n_3, n_4, a, b, c, d))
