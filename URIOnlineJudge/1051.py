rea = 0.0
sal = float(raw_input())
if sal <= 2000.00:
	print "Isento"
elif sal > 2000.00 and sal <= 3000.00:
	rea += (sal-2000.00)*0.08
	print "R$ %.2f" %rea
elif sal >3000.00 and sal <= 4500.00:
	rea += 1000.00*0.08
	rea += (sal-3000.00)*0.18
	print "R$ %.2f" %rea
elif sal > 4500.00:
	rea += 1000.00*0.08
	rea += 1500.00*0.18
	rea += (sal-4500.00)*0.28
	print "R$ %.2f" %rea