n = int(input())

for _ in range(n):
    x = int(input())
    s = 0
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            s += i
            if i != x // i:
                s += x // i
    if s == 2 * x:
        print(x, "is perfect")
    else:
        print(x, "is not perfect")
