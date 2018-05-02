n = int(raw_input())

for i in xrange(n):
    t = int(raw_input())
    tiros = map(int, raw_input().split())
    pulos = raw_input()

    cont = 0
    for j in xrange(len(tiros)):
        if (tiros[j] <= 2 and pulos[j] == 'S') or (tiros[j] >= 3 and pulos[j] == 'J'):
            cont += 1

    print cont