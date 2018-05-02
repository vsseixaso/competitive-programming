T = int(raw_input())
Fib=[]
Fib.append(0)
Fib.append(1)

aux=[]

for i in range (0, 59, 1):
	Fib.append(1)
	Fib[i+2] = Fib[i] + Fib[i+1]	

for i in range (0, T, 1):		
	N = int(raw_input())
	if N<=60 and N>=0:		
		print "Fib(%d) = %d" %(N, Fib[N])