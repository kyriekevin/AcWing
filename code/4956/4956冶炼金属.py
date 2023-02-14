if __name__ == "__main__":
    n = int(input())
    minv, maxv = 1, int(1e9)
    for _ in range(n):
        x, y = map(int, input().split())

        l, r = 1, int(1e9)
        while l < r:
            mid = l + r >> 1
            if x // mid <= y:
                r = mid
            else:
                l = mid + 1
        minv = max(minv, l)

        r = int(1e9)
        while l < r:
            mid = l + r + 1 >> 1
            if x // mid >= y:
                l = mid
            else:
                r = mid - 1
        maxv = min(maxv, l)
    print(minv, maxv)

