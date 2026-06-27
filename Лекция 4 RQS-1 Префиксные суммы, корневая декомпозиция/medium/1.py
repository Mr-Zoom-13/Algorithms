# https://informatics.msk.ru/mod/statements/view.php?id=43201&chapterid=2772#1
N, M, K = map(int, input().split())
a = []
prefs = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    a.append(tmp)
    prefs.append([0])
    for i in range(M):
        prefs[-1].append(prefs[-1][-1] + tmp[i])

square_prefs = [[0] * (M + 1), prefs[0]]
for x2 in range(2, N + 1):
    square_prefs.append([0])
    for y2 in range(1, M + 1):
        ans = square_prefs[x2 - 1][y2] + prefs[x2 - 1][y2]
        square_prefs[-1].append(ans)

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    ans = square_prefs[x2][y2]
    ans -= square_prefs[x2][y1 - 1]
    ans -= square_prefs[x1 - 1][y2]
    ans += square_prefs[x1 - 1][y1 - 1]
    print(ans)

