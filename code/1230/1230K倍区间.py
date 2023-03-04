if __name__ == "__main__":
    n, m = map(int, input().split())
    g, cnt = [0] * (n + 10), [0] * (n + 10)
    for i in range(1, n + 1):
        g[i] = int(input())
        g[i] += g[i - 1]

    cnt[0] = 1
    res = 0
    for i in range(1, n + 1):
        res += cnt[g[i] % m]
        cnt[g[i] % m] += 1
    print(res)
    
