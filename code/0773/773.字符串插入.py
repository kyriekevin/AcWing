from sys import stdin

for line in stdin.readlines():
    a, b = line.strip().split()
    idx = a.find(max(a))
    print(a[:idx + 1] + b + a[idx + 1:])
