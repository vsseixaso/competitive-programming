len_stripe = int(raw_input())
l = map(int, raw_input().split())

s1 = 0
s2 = 0
cont = 0

for i in range(len(l)):
	s2 += l[i]
        
for i in range(len(l)-1):
	s1 += l[i]
	s2 -= l[i]
	if s1 == s2:
		cont += 1

print cont
