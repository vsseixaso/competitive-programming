import math

n = int(raw_input())
for j in xrange(n):
    x = int(raw_input())

    if x == 1:
        print 'Not Prime'
    else:
        cont = 0
        for i in xrange(1, int(math.sqrt(x))+1):
            if x%i == 0:
                cont += 1

        if cont > 1:
            print 'Not Prime'
        else:
            print 'Prime'
