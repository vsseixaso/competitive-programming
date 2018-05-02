import math

a, b, c = map(float, raw_input().split())

if a>abs(b-c) and a<b+c and b>abs(a-c) and b<a+c and c>abs(b-c) and c<(b+c):
	perimetro = a+b+c
	print "Perimetro = %.1f" %perimetro
else:
	area = ((a+b)*c)/2
	print "Area = %.1f" %area