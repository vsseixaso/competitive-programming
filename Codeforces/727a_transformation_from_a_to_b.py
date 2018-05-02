way = []

def bpa(a,b):
	bstr = str(b)
	if b < a:
		return 'NO'
	elif b == a:
		return 'YES'
	elif b%2 == 1:
		if len(bstr) > 1:
			if bstr[-1] == '1':
				b = int(bstr[:-1])
				way.append(b)
				bpa(a,b)
			else:
				return 'NO'
	elif b%2 != 0:
		return 'NO'
	else:
		b = b/2
		way.append(b)
		bpa(a,b)

a, b = map(int, raw_input().split())

bpa(a,b)

if len(way) == 0:
	print 'NO'
elif way[-1] != a:
	print 'NO'
else:
	print 'YES'
	way = way[::-1]
	way.append(b)
	print len(way)
	way = map(str, way)
	print ' '.join(way)