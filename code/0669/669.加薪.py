n = float(input())

if n >= 0 and n <= 400:
    m = 0.15
elif n >= 400.01 and n <= 800:
    m = 0.12
elif n >= 800.01 and n <= 1200:
    m = 0.1
elif n >= 1200.01 and n <= 2000:
    m = 0.07
else:
    m = 0.04

print("Novo salario: %.2f" % (n * (1 + m)))
print("Reajuste ganho: %.2f" % (n * m))
print("Em percentual: %d %%" % (m * 100))
