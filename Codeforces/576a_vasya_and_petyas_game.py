mport math

n = 10**3
prime = [True] * (n + 1)
prime[0] = False
prime[1] = False
m = int(math.sqrt(n))

for i in range(2, m+1, 1):
	if (prime[i]):
		for k in range(i+i, n+1, i):
			prime[k] = False

a = input()
perguntas = []
for i in xrange(1, a + 1):
	if prime[i]:
		k = 1
		while k <= (a / i):
			k *= i
			perguntas.append(k)

print len(perguntas)
for i in perguntas:
	print i,