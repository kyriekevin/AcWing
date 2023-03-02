if __name__ == "__main__":
    n = int(input())
    g = list(map(int, input().split()))
    cnt = [0] * 100010

    j, res = 0, 0
    for i in range(n):
        cnt[g[i]] += 1
        while cnt[g[i]] > 1:
            cnt[g[j]] -= 1
            j += 1
        res = max(res, i - j + 1)
    print(res)
