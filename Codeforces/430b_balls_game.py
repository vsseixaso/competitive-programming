def organizaListas(lista):
	cor = [lista[0]]
	quant = [1]
	for i in range(len(lista)-1):
		if lista[i] == lista[i+1]:
			quant[-1] += 1
		else:
			cor.append(lista[i+1])
			quant.append(1)
	return cor, quant

n, k, x = map(int, raw_input().split())
bolas = map(int, raw_input().split())
destruidas = []
cor, quant = organizaListas(bolas)

for i in range(len(cor)):
	if cor[i] == x and quant[i] == 2:
		destruidas.append(2)
		j = i-1
		k = i+1
		while j >= 0 and k < len(cor) and cor[j] == cor[k] and quant[j] + quant[k] >= 3:
			destruidas[-1] += quant[j] + quant[k]
			j-=1
			k+=1
if len(destruidas) > 0:
	print max(destruidas)
else: print 0