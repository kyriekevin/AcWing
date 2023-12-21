def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i


a, b = map(int, input().split())
print(gcd(a, b))
