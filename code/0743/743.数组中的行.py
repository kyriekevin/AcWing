n = int(input())
t = input()

arr = [list(map(float, input().split())) for _ in range(12)]

s = sum(arr[n])
if t == "M":
    print("%.1f" % (s / 12))
else:
    print("%.1f" % s)
