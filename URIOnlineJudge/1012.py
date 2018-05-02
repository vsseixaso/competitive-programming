pi = 3.14159

A, B, C = map(float, raw_input().split())
triang = float((A*C))/2
circ = float(C**2)*pi
trap = float((A+B)*C)/2
quad = B**2
retang = A*B

print "TRIANGULO: %.3f" %triang
print "CIRCULO: %.3f" %circ
print "TRAPEZIO: %.3f" %trap
print "QUADRADO: %.3f" %quad
print "RETANGULO: %.3f" %retang