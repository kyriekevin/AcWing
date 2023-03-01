if __name__ == "__main__":
    n = int(input())
    s = input()

    res, cnt = 0, 0
    for i in range(n):
        if s[i] == 'x':
            cnt += 1
        else:
            cnt = 0
        if cnt >= 3:
            res += 1
            cnt -= 1
    print(res)
