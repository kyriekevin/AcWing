def cmp(a, b):
    if len(a) != len(b):
        return len(a) > len(b)

    for x, y in zip(a[::-1], b[::-1]):
        if x != y:
            return x > y
    return True

def sub(a, b):
    res = []
    t = 0
    for i in range(len(a)):
        t = a[i] - t
        if i < len(b):
            t -= b[i]
        res.append((t + 10) % 10)
        t = (t < 0)

    while (len(res) > 1 and res[-1] == 0):
        res.pop()

    return res

if __name__ == "__main__":
    a = list(map(int, input()))[::-1]
    b = list(map(int, input()))[::-1]

    if cmp(a, b):
        res = sub(a, b)
    else:
        res = sub(b, a)
        print("-", end="")

    print(''.join(map(str, res[::-1])))
