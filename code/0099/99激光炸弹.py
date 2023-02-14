N = 5010
s = [[0] * N for _ in range(N)]

if __name__ == "__main__":
    n, r = map(int, input().split())
    r = min(r, 5001)
    
    for _ in range(n):
        x, y, w = map(int, input().split())
        x += 1
        y += 1
        s[x][y] += w
    
    for i in range(1, 5002):
        for j in range(1, 5002):
            s[i][j] += s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1];
    
    res = 0
    for i in range(r, 5002):
        for j in range(r, 5002):
            res = max(res, s[i][j] - s[i - r][j] - s[i][j - r] + s[i - r][j - r])
    print(res)
