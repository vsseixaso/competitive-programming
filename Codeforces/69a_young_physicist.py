# coding: utf-8

# AA Básico 16.2 | CCC UFCG
# Vinícius Souza Seixas de Oliveira
# Young Physicist

n = int(raw_input())
x = []
y = []
z = []
for i in range(n):
    xi, yi, zi = map(float, raw_input().split())
    x.append(xi)
    y.append(yi)
    z.append(zi)
if sum(x) == 0 and sum(y) == 0 and sum(z) == 0:
    print 'YES'
else: 
    print 'NO'