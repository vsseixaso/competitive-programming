def prime(limit):
    limitn = limit+1
    not_prime = [False] * limitn
    primes = []
    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in xrange(i*2, limitn, i):
            not_prime[f] = True
        primes.append(i)
    return primes

def verifica(n1, n2, lista):
    
    i = 0
    while max(n1,n2) > lista[i] and i < len(lista)-1:
        if n1 % lista[i] == 0 and n2 % lista[i] == 0:
            return True
        i += 1
    return False

primos = prime(22000)
entrada = int(raw_input())
elemento = raw_input().split()
cont = 0
i = 0
while i < len(elemento)-1:

    resto = max(int(elemento[i]), int(elemento[i+1])) % min(int(elemento[i]), int(elemento[i+1]))

    if elemento[i] == '1' or elemento[i+1] == '1':
        pass
        
    elif resto == 0:
        elemento.insert(i+1,'1')
        cont += 1
        
    elif verifica(int(elemento[i]), int(elemento[i+1]), primos) ==  True:
        elemento.insert(i+1,'1')
        cont += 1
        
    i += 1

print cont
print " ".join(elemento)