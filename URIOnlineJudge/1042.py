a, b, c = map(int, raw_input().split())
aux1 = a
aux2 = b
aux3 = c
if a>b:
	a1 = b
	b = a
	a = a1
if b>c:
	a1 = c
	c = b
	b = a1
if a > b:
	a1 = b
	b = a
	a = a1
print a
print b
print c
print
print aux1
print aux2
print aux3