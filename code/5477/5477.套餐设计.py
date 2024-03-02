N = 110
n, m = map(int, input().split())
cnt = [0] * N
arr = list(map(int, input().split()))
for i in range(m):
    cnt[arr[i]] += 1


def check(x):
    tot = 0
    for i in range(1, N):
        tot += cnt[i] // x
    return tot >= n


l, r = 0, m // n
while l < r:
    mid = l + r + 1 >> 1
    if check(mid):
        l = mid
    else:
        r = mid - 1

print(l)
