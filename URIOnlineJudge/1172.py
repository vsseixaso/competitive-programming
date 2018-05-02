X= []
for i in range (0,10,1):
	X.append(int(raw_input()))
	if X[i]<=0:
		X[i]=1
	

for i in range (0,10,1):
	print "X[%d] = %d" %(i,X[i])