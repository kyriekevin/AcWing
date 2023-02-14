t = input()

arr = [list(map(float, input().split())) for _ in range(12)]

s, c = 0, 0
for i in range(12):
    for j in range(i + 1, 12):
        s += arr[i][j]
        c += 1

if t == "S":
    print("{:.1f}".format(s))
else:
    print("{:.1f}".format(s / c))
