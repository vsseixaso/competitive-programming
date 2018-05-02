a, b = map(int, raw_input().split())

if a < b:
    menor = a
else:
    menor = b

fat = 1
for i in xrange(1, menor+1):
    fat *= i

print fat