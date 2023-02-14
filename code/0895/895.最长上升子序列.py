n = int(input())
arr = list(map(int, input().split()))
f = [0] * n

for i in range(n):
    f[i] = 1
    for j in range(i):
        if arr[j] < arr[i]:
            f[i] = max(f[i], f[j] + 1)

print(max(f))
