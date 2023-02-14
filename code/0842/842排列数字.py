def dfs(u):
    global g, st
    if u == n:
        print(' '.join(map(str, g)))
        return

    for i in range(1, n + 1):
        if not st[i]:
            g[u] = i
            st[i] = True
            dfs(u + 1)
            st[i] = False


if __name__ == "__main__":
    n = int(input())
    g, st = [0] * n, [False for _ in range(n + 1)]
    dfs(0)
