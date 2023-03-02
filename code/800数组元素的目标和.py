if __name__ == "__main__":
    n, m, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    i, j = 0, m - 1
    while i < n and j >= 0:
        if a[i] + b[j] == x:
            print(i, j)
            break
        elif a[i] + b[j] > x:
            j -= 1
        else:
            i += 1
