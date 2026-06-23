# https://codeforces.com/contest/1463/problem/A
t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if (a + b + c) % 9 == 0:
        k = (a + b + c) // 9
        if a >= k and b >= k and c >= k:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
