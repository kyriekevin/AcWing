def check(m):
    S = set()
    for i in range(n - m + 1):
        cur = s[i: i + m]
        if cur in S:
            return False
        S.add(cur)
    return True


if __name__ == "__main__":
    n = int(input())
    s = input()

    l, r = 1, n
    while l < r:
        mid = l + r >> 1
        if check(mid):
            r = mid
        else:
            l = mid + 1

    print(l)
