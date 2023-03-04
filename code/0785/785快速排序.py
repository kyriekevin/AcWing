def quick_sort(g, s, e):
    if s >= e:
        return
    x, l, r = g[(s + e) // 2], s - 1, e + 1
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

    quick_sort(g, s, r)
    quick_sort(g, r + 1, e)

if __name__ == "__main__":
    n = int(input())
    g = list(map(int, input().split()))
    quick_sort(g, 0, n - 1)
    print(" ".join(map(str, g)))
