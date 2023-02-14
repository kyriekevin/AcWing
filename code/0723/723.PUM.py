n, m = map(int, input().split())

for i in range(n):
    for j in range(m):
        if j == m - 1:
            print("PUM")
        else:
            print(i * m + j + 1, end=" ")
