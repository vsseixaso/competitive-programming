n, x0, y0 = map(int, raw_input().split())
storms = []
for i in xrange(n):
	storms.append(map(int, raw_input().split()))

shots = 0
for j in xrange(n):
	if storms[j]:
		han = [x0, y0]
		alvo = storms[j]
		shots += 1
		storms[j] = False
		
		i = j + 1
		while i < n:
			mAlvo = storms[i]
			if mAlvo:
				if (alvo[0] - han[0])*(mAlvo[1] - han[1]) == (mAlvo[0] - han[0])*(alvo[1] - han[1]):
					storms[i] = False
			i += 1

print shots