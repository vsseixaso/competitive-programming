import math

c = int(raw_input())

for i in xrange(c):
    l = float(raw_input())
    x = (5*(l*l)/4) * (1/math.tan(math.pi / 5))
    ans = float("{0:.3f}".format(x))

    passouPonto = False
    aux = str(ans)
    count = 0
    for i in xrange(len(aux)):
        if aux[i] == '.':
            passouPonto = True

        if passouPonto:
            count += 1

    for i in xrange(count, 4):
        aux += '0'

    print aux
