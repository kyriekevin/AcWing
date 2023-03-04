if __name__ == "__main__":
    n = int(input())
    g = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        g[i] += g[i - 1]

    if g[n] % 3:
        print(0)
    else:
        res, cnt = 0, 0
        for i in range(2, n):
            if g[i - 1] * 3 == g[n]:
                cnt += 1
            if g[i] * 3 == g[n] * 2:
                res += cnt
        print(res)
        
