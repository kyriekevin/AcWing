def check(s, c):
    res = []
    bk = list(s)
    for i in range(n - 1):
        if bk[i] != c:
            res.append(i)
            bk[i] = 'B' if bk[i] == 'W' else 'W'
            bk[i + 1] = 'B' if bk[i + 1] == 'W' else 'W'

    if bk[-1] != c:
        return False

    print(len(res))
    for x in res:
        print(x + 1, end=' ')
    if res:
        print()

    return True


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        s = input()
        if not check(s, 'W') and not check(s, 'B'):
            print(-1)
