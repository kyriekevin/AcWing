h, w = [], []


def check(x):
    cnt = 0
    for i in range(n):
        cnt += (h[i] // x) * (w[i] // x)
        if cnt >= k:
            return True

    return False


if __name__ == "__main__":
    n, k = map(int, input().split())
    for i in range(n):
        a, b = map(int, input().split())
        h.append(a)
        w.append(b)

    l, r = 1, int(1e5)
    while l < r:
        mid = l + r + 1 >> 1
        if check(mid):
            l = mid
        else:
            r = mid - 1

    print(l)
