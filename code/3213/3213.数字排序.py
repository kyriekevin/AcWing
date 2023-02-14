_ = int(input())
d = {}
for x in map(int, input().split()):
    d[x] = d.get(x, 0) + 1
a = sorted(d.items(), key=lambda x: (-x[1], x[0]))
for k, v in a:
    print(k, v)
