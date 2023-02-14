n, m, x = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i, j = 0, len(b) - 1
while i < n and j >= 0:
    if a[i] + b[j] == x:
        print(i, j)
        break
    elif a[i] + b[j] < x:
        i += 1
    else:
        j -= 1
