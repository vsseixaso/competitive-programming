def soma_algarismos(x):
    soma = 0
    for i in xrange(len(x)):
        soma += int(x[i])

    if len(str(soma)) > 1:
        return soma_algarismos(str(soma))
    else:
        return soma

while True:
    n, m = raw_input().split()

    if n == m == '0': break

    a = soma_algarismos(n)
    b = soma_algarismos(m)

    if a > b:
        print 1
    elif a < b:
        print 2
    else:
        print 0