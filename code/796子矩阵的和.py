if __name__ == "__main__":
    n, m, q = map(int, input().split())
    a = [[0] * (m + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    s = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = s[i - 1][j] + s[i][j - 1] + a[i][j] - s[i - 1][j - 1]
    
    for query in queries:
        x1, y1, x2, y2 = query
        print(s[x2][y2] - s[x1 - 1][y2] - s[x2][y1 - 1] + s[x1 - 1][y1 - 1])
