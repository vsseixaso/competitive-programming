vogais = ['a', 'e', 'i', 'o', 'u', 'y']

ent = raw_input()

ent = ent.lower()
out = ''
for i in xrange(len(ent)):
    if ent[i] not in vogais:
        out += '.' + ent[i]

print out