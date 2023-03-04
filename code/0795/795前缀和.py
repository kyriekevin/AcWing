if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        g[i] += g[i - 1]
    for _ in range(m):
        l, r = map(int, input().split())
        print(g[r] - g[l - 1])
        
