t = input()

arr = [list(map(float, input().split())) for _ in range(12)]

s, c = 0, 0
for i in range(5):
    for j in range(i + 1, 11 - i):
        s += arr[i][j]
        c += 1

if t == "M":
    s /= c

print("%.1f" % s)
