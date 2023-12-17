while True:
    n = int(input())
    if n == 0:
        break

    for i in range(n):
        for j in range(n):
            x = min(i, j, n - i - 1, n - j - 1) + 1
            print(x, end=" ")
        print()

    print()
