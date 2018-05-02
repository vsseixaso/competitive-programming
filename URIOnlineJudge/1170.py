n = int(raw_input())
lista = []
for i in range(n):
    ent = float(raw_input())
    lista.append(ent)

for i in range(len(lista)):
    count = 0
    aux = lista[i]
    while aux > 1.0:
        aux = aux/2
        count += 1
    print count, "dias"