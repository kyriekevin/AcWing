def dfs(x, y, u, cur):
    if u > k:
        res.add(cur)
        return

    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
    for i in range(4):
        a, b = x + dx[i], y + dy[i]
        if a < 0 or a >= n or b < 0 or b >= m:
            continue
        dfs(a, b, u + 1, 10 * cur + g[x][y])


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(n)]
    res = set()
    for i in range(n):
        for j in range(m):
            dfs(i, j, 0, 0)
    print(len(res))
