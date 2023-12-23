n = int(input())
d = {}
for _ in range(n):
    s, c = input().split()
    d[s] = c
n = int(input())
for _ in range(n):
    s = input()
    print(d.get(s, -1))
