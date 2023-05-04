if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        w = list(map(int, input().split()))
        cnt = [0] * 210
        for i in range(n):
            cnt[w[i]] += 1

        res = 0
        for i in range(n):
            for j in range(n):
                res += cnt[w[i] + w[j]]
        print(res)
