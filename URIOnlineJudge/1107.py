entrada = raw_input().split()
a =int(entrada[0])
c =int(entrada[1])

while(a != 0 and c!=0):
	resposta=0;
	block=raw_input().split()
	for i in range(c):
		if(i==0):
			if(int(block[i])<a):
				resposta+=(a-int(block[i]))
		else:
			if(int(block[i]) < int(block[i-1])):
				resposta+=(int(block[i-1])-int(block[i]))
	print(resposta);
	entrada = raw_input().split()
	a =int(entrada[0])
	c =int(entrada[1])