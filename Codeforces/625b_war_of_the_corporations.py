# coding: utf-8

# AA Básico 16.2 | CCC UFCG
# Vinícius Souza Seixas de Oliveira
# War of the Corporations

x = raw_input()
y = raw_input()

if len(y) > len(x):
        print 0
elif y == x:
        print 1
else:
        count = 0
        i = 0
        while i <= len(x)-len(y):
                if x[i:len(y)+i] == y:
                        count += 1
                        i += len(y)  
                else:
                        i+=1
        print count