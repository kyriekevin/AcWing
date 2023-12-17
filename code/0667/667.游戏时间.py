a, b = map(int, input().split())
if a == b:
    print("O JOGO DUROU 24 HORA(S)")
else:
    print("O JOGO DUROU %d HORA(S)" % ((b - a) % 24))
