def div(a, b):
    res = []
    t, r = 0, 0
    for i in range(len(a)):
        t = 10 * r + a[i]
        res.append(t // b)
        r = t % b

    while len(res) > 1 and res[0] == 0:
        res.pop(0)

    return res, r

if __name__ == "__main__":
    a = list(map(int, input()))
    b = int(input())
    res, r = div(a, b)
    print(''.join(map(str, res)))
    print(r)
    
    
