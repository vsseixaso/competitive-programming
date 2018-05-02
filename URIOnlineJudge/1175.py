N=[]
for i in range (0, 20, 1):
	v = int(raw_input())
	N.append(v)
	
aux=0
for i in range (0, 10, 1):
		aux = N[19-i]
		N[19-i] = N[i]
		N[i] = aux
	

for i in range  (0, 20, 1):
	print "N[%d] = %d" %(i, N[i])