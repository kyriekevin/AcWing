from math import sqrt
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
print("%.4f" % sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))
