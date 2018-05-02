a=1
b=0
while a<=5:
	v = float(raw_input())
	if v%2==0:
		b+=1
	a+=1
print "%d valores pares" %b