n = int(input())
s = set()
for _ in range(n):
    a, b = input().split()
    b = int(b)
    if a == "I":
        s.add(b)
    else:
        print("Yes" if b in s else "No")
