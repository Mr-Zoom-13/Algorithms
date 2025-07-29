# https://informatics.msk.ru/mod/statements/view.php?id=1966&chapterid=1620#1


N, R, C = [int(i) for i in input().split()]
students = []
for i in range(N):
    students.append(int(input()))
students.sort()
print(students)

