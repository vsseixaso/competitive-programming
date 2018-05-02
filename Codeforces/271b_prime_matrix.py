#coding: utf-8

def primes(DIM):

	vals=[True] * DIM
	
	vals[0]=False
	vals[1]=False
	 
	for i in range(2,DIM):
		
		if vals[i]:			
			j = i * i			
			while True :
				
				if j >= DIM : 
					break
							
				vals[j] = False							
				j += i			
	return vals
	

primes = primes(10 ** 5 + 100)
lista = [0,1,0]

for i in range(3,10 ** 5  + 100):
	
	count = 0
	if not(primes[i]) :
			
			x = i + 1
			
			count += 1

			while x < (10 ** 5 + 100) :
				
				if primes[x]   :
					break
				
				x += 1
				count += 1
	
	lista.append(count)

n , m = map(int,raw_input().split())
matrix = []
moves = []

for i in range(n):
	
	matrix.append(map(int,raw_input().split()))
	
	count = 0
	
	for j in range(m) :
		
		count += lista[matrix[i][j]]
				
	moves.append(count)


if min(moves) == 0 :
	
	print 0

else :
	
	for i in range(m):	
	
		count = 0
		
		for j in range(n) :
		
			count += lista[matrix[j][i]]
				
		moves.append(count)
	
	print min(moves)