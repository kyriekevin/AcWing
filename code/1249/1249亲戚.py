from sys import stdin

N = int(2e4 + 10)
p = [i for i in range(N)]


def find(x):
    if p[x] != x:
        p[x] = find(p[x])

    return p[x]


if __name__ == "__main__":
    n, m = map(int, input().split())

    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        p[find(a)] = find(b)

    q = int(input())
    for _ in range(q):
        a, b = map(int, stdin.readline().split())
        if find(a) != find(b):
            print('No')
        else:
            print('Yes')
