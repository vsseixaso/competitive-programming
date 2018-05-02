def saida(lista):
        saida = ''
        for i in range(len(lista)):
                x = str(lista[i])
                if i < len(lista)-1:
                        saida += x
                        saida += ' '
                else: saida += x
        return saida

n = int(raw_input())

for k in range(n):
        lista = []
        for i in range(5):
                ent = map(int, raw_input().split())
                if len(ent) != 1:
                        for j in range(0,len(ent),2):
                                ent.insert(j+1,0)
                if len(ent) == 6: ent.insert(5,0)
                if len(ent) == 8: ent.insert(7,0)
                lista.append(ent)
                if i < 4:
                        lista.append([0]*(i+1)*2)

        i = 0
        j = 1
        for m in range(4):
                x = lista[6][i]
                y = lista[8][i]
                z = lista[8][i+2]
                lista[8][j] = (x-y-z)/2
                i += 2
                j += 2

        for i in range(8,-1,-1):
                for j in range(len(lista[i])-1):
                        x = lista[i][j]
                        y = lista[i][j+1]
                        lista[i-1][j] = x + y

        for i in range(len(lista)):
                 print saida(lista[i])