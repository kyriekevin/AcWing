a = float(input())
b = [100, 50, 20, 10, 5, 2, 1]
print(int(a))
cnt = 0

for i in b:
    while a // i != 0:
        cnt += 1
        a -= i
    print("%d nota(s) de R$ %d,00" % (cnt, i))
    cnt = 0
