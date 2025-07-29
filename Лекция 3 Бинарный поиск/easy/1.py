# https://informatics.msk.ru/mod/statements/view.php?id=1966#1


def check(side):
    for_w = side // w
    for_h = side // h
    if for_w * for_h >= n:
        return True
    return False


w, h, n = [int(i) for i in input().split()]
l = 0
r = 10**20
while r - l != 1:
    m = l + (r - l) // 2
    if check(m):
        r = m
    else:
        l = m
print(r)