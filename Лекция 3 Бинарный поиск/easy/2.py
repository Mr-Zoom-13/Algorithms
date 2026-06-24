# https://informatics.msk.ru/mod/statements/view.php?id=1966&chapterid=894#1
import random
from math import ceil

def binary_search(l, r, v, d, n, distances, times):
    for _ in range(100):  # выполняем ровно 100 итераций
        m = l + (r - l) / 2
        if func(m, v, d, n, distances, times):
            r = m
        else:
            l = m
    return r


def func(ans, v, d, n, distances, times):
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


def get_answer(v, d, n, arr):
    if n == 0:
        return to_time_format(0)
    distances = []
    times = []
    for i in range(n):
        this_str = arr[i].split()
        distances.append(int(this_str[0]))
        times.append(int(this_str[1].split(":")[0]) * 60 + int(this_str[1].split(":")[1]))
    result_wait = binary_search(0, 1500, v, d, n, distances, times)
    answer = ceil(result_wait + distances[-1] * 2 / v + n * d)
    return to_time_format(answer)



# f(r) >= target, f(l) < target by function contract
def binarySearch(f, l, r, target):
    assert f(l) < target
    assert f(r) >= target
    for _ in range(100):
        m = l + (r - l) / 2
        if target == f(m):
            return m
        elif target < f(m):
            r = m
        else:
            l = m
    return r


def f(wait_time, dist, times, v, d):
    total_time = wait_time
    if not dist:
        return total_time
    for i in range(len(dist) - 1):
        total_time += dist[i] / v
        if total_time >= times[i]:
            total_time += d
    total_time += dist[-1] / v
    return total_time


def solve(dist, times, v, d, last, n):
    def g(wait_time):
        return f(wait_time, dist, times, v, d)

    # let's find the least possible wait_time, that results in total_time
    # bigger or equal than times[-1]
    if g(0) < max(times):  # max(times) == times[-1]
        ans_time = binarySearch(g, 0, max(times), max(times))
    else:
        ans_time = 0

    t = ans_time + 2 * last / v + n * d
    t = int(t) + (t % 1 > 0)  # equivalent to t = math.ceil(t)
    hours, minutes = str(t // 60), str(t % 60)
    hours = "0" * (2 - len(hours)) + hours
    minutes = "0" * (2 - len(minutes)) + minutes
    return f"{hours}:{minutes}"


def test_solve():
    pass


def get_right_answer(v, d, n, arr):
    dist = []
    times = []
    last = 0
    for i in range(n):
        x, t = arr[i].split()
        x = int(x)
        h, m = [int(s) for s in t.split(":")]
        dist.append(x - last)
        times.append(float(h * 60 + m))
        last = x
    return solve(dist, times, v, d, last, n)



def check_answers():
    for _ in range(1000):
        try:
            v = random.randint(1, 199)
            d = random.randint(0, 500)
            n = random.randint(0, 200)
            arr = []
            my_times = []
            my_x = []
            for i in range(n):

                if not arr:
                    random_time = random.randint(0, 1440)
                    my_times.append(random_time)
                    random_time = to_time_format(random_time)
                    x = random.randint(1, 32767)
                    my_x.append(x)
                else:
                    random_time = random.randint(my_times[-1] + 1, 1440)
                    my_times.append(random_time)
                    random_time = to_time_format(random_time)
                    x = random.randint(my_x[-1] + 1, 32767)
                    my_x.append(x)
                arr.append(f"{x} {random_time}")
        except:
            continue
        if get_answer(v, d, n, arr) != get_right_answer(v, d, n, arr):
            print(f"{v} {d} {n} {arr}")
            print(get_answer(v, d, n, arr))
            print(get_right_answer(v, d, n, arr))

print(get_right_answer(3,1, 1, ['100 00:01']))
print(get_answer(3,1, 1, ['100 00:01']))
print(check_answers())