# https://informatics.msk.ru/mod/statements/view.php?id=1966&chapterid=894#1

v, d = [int(i) for i in input().split()]
n = int(input())
s = 0
for i in range(n):
    rasst, time = input().split()
    s += int(rasst)


minutes = round(2 * s / v) + d * n
hours = "0" * (2 - len(str(minutes // 60))) + str(minutes // 60)
minutes = "0" * (2 - len(str(minutes % 60))) + str(minutes % 60)
print(f"{hours}:{minutes}")
