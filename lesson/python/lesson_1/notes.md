# 1. A + B
```python
print(sum(map(int, input().split())))
```

# 604. 圆的面积
```python
print("A=%.4f" % (3.14159 * (float(input())) ** 2))
```

# 606. 平均数1
```python
A = float(input())
B = float(input())
print("MEDIA = %.5f" % ((3.5 * A + 7.5 * B) / (3.5 + 7.5)))
```

# 616. 两点间的距离
```python
from math import sqrt
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
print("%.4f" % sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))
```

# 653. 钞票
```python
a = float(input())
b = [100, 50, 20, 10, 5, 2, 1]
print(int(a))
cnt = 0

for i in b:
    while a // i != 0:
        cnt += 1
        a -= i
    print("%d nota(s) de R$ %d,00" % (cnt, i))
    cnt = 0
```
