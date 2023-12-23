_ = int(input())
cnt = {}
for x in map(int, input().split()):
    cnt[x] = cnt.get(x, 0) + 1
    print(cnt[x], end=" ")
