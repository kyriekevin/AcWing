s = input()
n = len(s)
for i in range(n):
    print(chr(ord(s[i]) + ord(s[(i + 1) % n])), end="")
