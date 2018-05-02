a, b, n = map(int,raw_input().split())

if a % b == 0:
	for i in xrange(n):
		a *= 10

	print a
else:
	count = 0
	imprimir = ""
	for i in xrange(0,10,1):
		imprimir = str(a) + str(i)
		if int(imprimir) % b == 0:
			count = 1
			break
	if count == 0:
		print "-1"
	else:
		imprimir = int(imprimir)
		for i in xrange(n-1):
			imprimir *= 10
		print imprimir