def lowbit(x):
    return x & -x


if __name__ == "__main__":
    n = int(input())
    g = list(map(int, input().split()))
    for x in g:
        res = 0
        while x:
            x -= lowbit(x)
            res += 1
        print(res, end=' ')
