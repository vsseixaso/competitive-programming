livros = []
for i in range(5):
        ent = map(int, raw_input().split())
        ent.pop(0)
        livros.append(ent)
conj = int(raw_input())
combinacoes = []
total = 0

for i in livros[0]:
        for j in livros[1]:
                for k in livros[2]:
                        for l in livros[3]:
                                for m in livros[4]:
                                        combinacoes.append(i+j+k+l+m)
combinacoes.sort()
for i in xrange(conj):
        total += combinacoes[-(i+1)]
print total