import math

def calculaDistancia(d1,d2):
	if d1 >= 0 and d2 >= 0:
		return abs(d1-d2)
	elif d1 < 0 and d2 < 0:
		return abs(d1-d2)
	elif d1 <= 0 and d2 >= 0:
		return abs(d1)+d2
	else:
		return d1+abs(d2)

n = int(raw_input())
dist = map(int, raw_input().split())

saida = []
for i in range(n):
        if i == 0:
                aux1 = calculaDistancia(dist[0],dist[1])
                aux2 = calculaDistancia(dist[0],dist[-1])
		l = [aux1,aux2]
		mi = min(l)
		ma = max(l)
		saida.append([mi,ma])
	elif i == n-1:
		aux1 = calculaDistancia(dist[-1],dist[-2])
		aux2 = calculaDistancia(dist[-1],dist[0])
		l = [aux1,aux2]
                mi = min(l)
                ma = max(l)
                saida.append([mi,ma])
	else:
		aux1 = calculaDistancia(dist[i],dist[i-1])
		aux2 = calculaDistancia(dist[i],dist[i+1])
		l = [aux1,aux2]
		mi = min(l)
		aux1 = calculaDistancia(dist[i],dist[0])
		aux2 = calculaDistancia(dist[i],dist[-1])
		l = [aux1,aux2]
		ma = max(l)
		saida.append([mi,ma])

for i in range(len(saida)):
	print saida[i][0], saida[i][1]