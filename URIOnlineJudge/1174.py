A = []

for i in range (0, 100, 1):
	V = float(raw_input())
	A.append(V)

for i in range (0, 100, 1):
	if A[i]<=10:
		print "A[%d] = %.1f" %(i, A[i])