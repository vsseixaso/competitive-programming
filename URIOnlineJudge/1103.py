while True:
    linha = map(int, raw_input().split())

    if linha == [0, 0, 0, 0]:
        break

    x = 60 * linha[0] + linha[1]
    y = 60 * linha[2] + linha[3]

    if y <= x:
        y += 60 * 24

    print abs(x - y)