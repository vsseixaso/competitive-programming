while True:
    bancos, debenturas = map(int, raw_input().split())

    if bancos == debenturas == 0: break

    reservas = map(int, raw_input().split())

    for i in xrange(debenturas):
        devedor, credor, valor = map(int, raw_input().split())
        reservas[devedor-1] -= valor
        reservas[credor-1] += valor

    quitou = 'S'
    for i in xrange(len(reservas)):
        if reservas[i] < 0:
            quitou = 'N'

    print quitou
