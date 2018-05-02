a, b = map(int,raw_input().split())
x = 1

for i in range(1,11):
	
	if (a * i ) % 10 == 0 or (a * i ) % 10 == b :
		
		x = i
		break
		
	
print x