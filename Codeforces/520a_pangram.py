n = int(raw_input())

s = raw_input()
s = s.lower()
s = list(s)
s = set(s)

if len(s) == 26:
	print 'YES'
else:
	print 'NO'