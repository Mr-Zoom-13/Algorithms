# https://informatics.msk.ru/mod/statements/view.php?id=1966&chapterid=894#1
from math import ceil

def binary_search(l, r):
    for _ in range(1000):  # выполняем ровно 100 итераций
        m = l + (r - l) / 2
        if func(m):
            r = m
        else:
            l = m
    return r


def func(ans):
    global v, d, n, distances, times

    cur_time = ans
    cur_distance = 0
    for i in range(n - 1):
        # прибавляю сколько времени надо идти до i-того цветка
        cur_time += (distances[i] - cur_distance) / v

        if cur_time >= times[i]:
            cur_time += d

        cur_distance = distances[i]
    cur_time += (distances[-1] - cur_distance) / v
    if cur_time >= times[-1]:
        return True
    return False


def to_time_format(minutes):
    hours = str(minutes // 60)
    hours_str = "0" + hours if len(hours) == 1 else hours
    minutes = str(minutes % 60)
    minutes_str = "0" + minutes if len(minutes) == 1 else minutes
    return f"{hours_str}:{minutes_str}"


v, d = map(int, input().split())
n = int(input())
if n == 0:
    print(to_time_format(0))
    exit()
distances = []
times = []
for i in range(n):
    this_str = input().split()
    distances.append(int(this_str[0]))
    times.append(int(this_str[1].split(":")[0]) * 60 + int(this_str[1].split(":")[1]))

result_wait = binary_search(0, 1500)
answer = result_wait + distances[-1] * 2 / v + n * d
answer = int(answer) + (answer % 1 > 0)
print(to_time_format(answer))