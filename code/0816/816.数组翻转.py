n, s = map(int, input().split())
arr = list(map(int, input().split()))
print(" ".join(map(str, reversed(arr[:s]))) + " " + " ".join(map(str, arr[s:])))
