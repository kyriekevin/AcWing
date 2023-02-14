def quick_select(g, s, e, k):
    if s >= e:
        return g[s]
    x, l, r = g[s], s - 1, e + 1
    while l < r:
        while True:
            l += 1
            if g[l] >= x:
                break
        while True:
            r -= 1
            if g[r] <= x:
                break
        if l < r:
            g[l], g[r] = g[r], g[l]

    if r - s + 1 >= k:
        return quick_select(g, s, r, k)
    else:
        return quick_select(g, r + 1, e, k - (r - s + 1))

if __name__ == "__main__":
    n, m = map(int, input().split())
    g = list(map(int, input().split()))
    print(quick_select(g, 0, n - 1, m))
