if __name__ == "__main__":
    n = int(input())
    nums = list(input().split())
    g = [0] * 10
    res = 0
    for i in range(n):
        num = nums[i]
        l, r = ord(num[0]) - ord('0'), ord(num[-1]) - ord('0')
        f = max(1, g[l] + 1)
        g[r] = max(g[r], f)
        res = max(res, f)
    print(n - res)
