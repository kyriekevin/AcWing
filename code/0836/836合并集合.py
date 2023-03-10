def find(x):
    if p[x] != x:
        p[x] = find(p[x])

    return p[x]


if __name__ == "__main__":
    n, m = map(int, input().split())
    p = [i for i in range(n + 1)]

    for _ in range(m):
        op = input().split()
        a, b = find(int(op[1])), find(int(op[2]))
        if op[0] == 'M':
            p[b] = a
        else:
            print("Yes") if a == b else print("No")
