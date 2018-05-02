x = raw_input()
l = []
for i in xrange(len(x)):
    l.append(int(x[i]))

if l[0] < 9:
    if 9 - l[0] < l[0]:
        l[0] = 9 - l[0]

for i in xrange(1, len(l)):
    if 9 - l[i] < l[i]:
        l[i] = 9 - l[i]

ans = ""
for i in xrange(len(l)):
    ans += str(l[i])

print ans