n, m = map(int, raw_input().split())
names = []
for i in xrange(n):
    names.append(raw_input())

d = [""] * m
total = 0

for i in xrange(m):
    for j in xrange(n):
        if names[j][i] not in d[i]:
            d[i] += names[j][i]

total += len(d[0])
for i in xrange(1,m):
    total *= len(d[i])

print total % 1000000007