def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

nTests = int(raw_input())
for nt in xrange(1, nTests + 1):
    s1 = raw_input()
    s2 = raw_input()

    if gcd(int(s1, 2), int(s2, 2)) > 1:
        print 'Pair #%d: All you need is love!' % (nt)
    else:
        print 'Pair #%d: Love is not all you need!' % (nt)