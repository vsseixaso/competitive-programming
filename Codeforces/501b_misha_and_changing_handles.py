lista = []

n = int(raw_input())

def procura(old, lista):
	for i in range(len(lista)):
		if (lista[i][1] == old):
			return i
			
	return -99

for i in range(n):
	old, new = raw_input().split()
	
	index = procura(old, lista)
	
	if (len(lista) == 0 or index == -99):
		lista.append([old, new])
	else:
		lista[index][1] = new

print len(lista)
for names in lista:
	print names[0], names[1]