if __name__ == "__main__":
    x = float(input())
    l, r = -1e4, 1e4

    while r - l > 1e-8:
        mid = (l + r) / 2
        if mid ** 3 >= x:
            r = mid
        else:
            l = mid

    print("{:.6f}".format(l))
    
