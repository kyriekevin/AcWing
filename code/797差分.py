def insert(l, r, c):
    global b
    b[l] += c
    b[r + 1] -= c
    
if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    queries = [tuple(map(int, input().split())) for _ in range(m)]
    b = [0] * (n + 2)

    for i in range(1, n + 1):
        insert(i, i, a[i])

    for query in queries:
        insert(*query)

    for i in range(1, n + 1):
        b[i] += b[i - 1]

    print(' '.join(map(str, b[1: -1])))
    
