if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    i, j = 0, 0
    while i < n and j < m:
        if a[i] == b[j]:
            i += 1
        j += 1

    if i == n:
        print('Yes')
    else:
        print('No')
