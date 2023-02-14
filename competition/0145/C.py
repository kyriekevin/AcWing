n, k, l = map(int, input().split())
w = list(map(int, input().split()))
m = n * k

w.sort()
if w[n - 1] > w[0] + l:
    print("0")
else:
    i = n - 1
    while i < m and w[i] <= w[0] + l:
        i += 1

    right = m - i
    res = 0
    for j in range(n):
        can = min(right, k - 1)
        left = k - can
        right -= can
        i -= left
        res += w[i]

    print(res)
