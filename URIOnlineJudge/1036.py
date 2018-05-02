import math

A, B, C = map(float, raw_input().split())
delta = (B**2) - (4*A*C)
if A!=0 and delta>=0:
	R1 = ((-B) + (math.sqrt(delta)))/(2*A)
	R2 = ((-B) - (math.sqrt(delta)))/(2*A)
	print "R1 = %.5f" %R1
	print "R2 = %.5f" %R2
else:
	print "Impossivel calcular"