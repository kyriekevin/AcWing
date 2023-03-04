if __name__ == "__main__":
    n, q = map(int, input().split())
    g = list(map(int, input().split()))
    for _ in range(q):
        x = int(input())
        l, r = 0, n - 1
        while l < r:
            mid = l + r >> 1
            if g[mid] >= x:
                r = mid
            else:
                l = mid + 1
        
        if g[l] != x:
            print("-1 -1")
        else:
            print(l, end=" ")
            r = n - 1
            while l < r:
                mid = l + r + 1 >> 1
                if g[mid] <= x:
                    l = mid
                else:
                    r = mid - 1
            print(r)
