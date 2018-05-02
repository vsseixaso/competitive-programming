a, b = map(int, raw_input().split())
if a>b:
	if a%b==0:
		print "Sao Multiplos"
	else:
		print "Nao sao Multiplos"	
elif b>a:
	if b%a==0:
		print "Sao Multiplos"
	else:
		print "Nao sao Multiplos"
else:
	print "Sao multiplos"