n, m = map(int, raw_input().split())
if n>=1 and n<=100 and m>=1 and m<=100:
	a = min(n,m)
	if a%2==0:
		print "Malvika"
	else:
		print "Akshat"
