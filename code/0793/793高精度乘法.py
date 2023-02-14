def mul(a, b):
    res = []
    t, i = 0, 0

    while i < len(a) or t:
        if i < len(a):
            t += a[i] * b
            i += 1
        res.append(t % 10)
        t //= 10

    while len(res) > 1 and res[-1] == 0:
        res.pop()

    return res

if __name__ == "__main__":
    a = list(map(int, input()))[::-1]
    b = int(input())
    res = mul(a, b)
    print(''.join(map(str, res[::-1])))
    
