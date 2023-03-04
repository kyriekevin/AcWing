def add(a, b):
    c = []
    i, carry = 0, 0
    while i < max(len(a), len(b)) or carry:
        t1 = a[i] if i < len(a) else 0
        t2 = b[i] if i < len(b) else 0
        c.append((t1 + t2 + carry) % 10)
        carry = (t1 + t2 + carry) // 10
        i += 1

    return c

if __name__ == "__main__":
    a = list(map(int, input()))[::-1]
    b = list(map(int, input()))[::-1]
    c = add(a, b)
    print(''.join(map(str, c[::-1])))
    
