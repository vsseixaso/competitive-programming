cont = [0] * 7

ent = raw_input()
linha = []
for i in xrange(len(ent)):
    linha.append(ent[i])

for i in xrange(len(linha)):
    if linha[i] == 'B':
        cont[0] += 1
    elif linha[i] == 'u':
        cont[1] += 1
    elif linha[i] == 'l':
        cont[2] += 1
    elif linha[i] == 'b':
        cont[3] += 1
    elif linha[i] == 'a':
        cont[4] += 1
    elif linha[i] == 's':
        cont[5] += 1
    elif linha[i] == 'r':
        cont[6] += 1

cont[1] = cont[1]/2
cont[4] = cont[4]/2

cont.sort()
print cont[0]