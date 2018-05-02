a=1
b=0
s=0
while a<=6:
	v = float(raw_input())
	if v>0:
		s+=v	
		b+=1
	a+=1
m = s/b
print "%d valores positivos" %b
print "%.1f" %m