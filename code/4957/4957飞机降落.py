def dfs(u, last):
    if u == n:
        return True

    for i in range(n):
        a, b, c = t[i], d[i], l[i]
        if not st[i] and a + b >= last:
            st[i] = True
            if dfs(u + 1, max(last, a) + c):
                return True
            st[i] = False

    return False

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        st = [False] * n
        t, d, l = [], [], []
        for _ in range(n):
            a, b, c = map(int, input().split())
            t.append(a)
            d.append(b)
            l.append(c)

        if dfs(0, 0):
            print("YES")
        else:
            print("NO")
