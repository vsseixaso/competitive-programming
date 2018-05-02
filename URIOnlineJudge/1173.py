V = int(raw_input())

if V<=50:
	N = []
	N.append (V)

	for i in range (0, 10, 1):
		V*=2	
		N.append(V)
	
	for i in range (0, 10, 1):
		print "N[%d] = %d" %(i, N[i])