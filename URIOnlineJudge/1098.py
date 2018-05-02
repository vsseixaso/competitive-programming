a = 1
count = 0
I=0
b=0
J=1
count2 = 0
while a<=44:
	count +=1
	if count == 4:
		I+=0.2
		if I > 1.8:
			I = 2
		b=a/4
		J=1+(0.2*b)
		count = 0
		count2+=1
	else:
		if type(I) is float and I<=1.8 and count2%5 != 0: 		
			print "I=%.1f J=%.1f" %(I,J)
		else:
			print "I=%d J=%d" %(I,J)
			
		J+=1.0
	a+=1