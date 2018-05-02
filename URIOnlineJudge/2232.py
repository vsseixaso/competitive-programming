t = int(raw_input())
ent = []
for i in xrange(t):
    n = int(raw_input())
    ent.append(n)

c_sum = [1]
for i in xrange(1, 32):
    c_sum.append(2**i + c_sum[i-1])

for i in xrange(t):
    print c_sum[ent[i]-1]