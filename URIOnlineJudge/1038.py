cod, quant = map(int, raw_input().split())
if cod==1:
	v=4.00
elif cod==2:
	v=4.50
elif cod==3:
	v=5.00
elif cod==4:
	v=2.00
elif cod==5:
	v=1.50
total = v*quant
print "Total: R$ %.2f" %total