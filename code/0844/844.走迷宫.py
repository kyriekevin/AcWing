n, m = map(int, input().split())
d = [[0] * m for _ in range(n)]
g = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
q = []

q.append((0, 0))

while len(q):
    sz = len(q)
    for _ in range(sz):
        x, y = q[0]
        q.pop(0)
        for i in range(4):
            a, b = x + dx[i], y + dy[i]
            if a < 0 or a >= n or b < 0 or b >= m or g[a][b] == 1 or d[a][b]:
                continue
            q.append((a, b))
            d[a][b] = d[x][y] + 1
print(d[-1][-1])
