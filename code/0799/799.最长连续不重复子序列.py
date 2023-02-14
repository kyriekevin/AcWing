n = int(input())
arr = list(map(int, input().split()))
cnt = [0] * 100010
l, res = 0, 0

for r in range(n):
    cnt[arr[r]] += 1
    while cnt[arr[r]] > 1:
        cnt[arr[l]] -= 1
        l += 1
    res = max(res, r - l + 1)
print(res)
