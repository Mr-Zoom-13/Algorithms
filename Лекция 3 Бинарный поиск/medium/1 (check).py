import matplotlib.pyplot as plt

T = int(input())
for _ in range(T):
    n = int(input())
    x = list(map(int, input().split()))
    t = list(map(int, input().split()))
    lst_x = []
    lst_y = []
    for c in range(0, 20):
        cur_time = 0
        for i in range(n):
            cur_time = max(cur_time, t[i] + abs(c - x[i]))
        lst_x.append(c)
        lst_y.append(cur_time)
        print(f"{c}: {cur_time}")
    print(lst_x)
    print(lst_y)


    plt.plot(lst_x, lst_y)
    plt.show()