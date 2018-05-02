# coding: utf-8

# AA Básico 16.2 | CCC UFCG
# Vinícius Souza Seixas de Oliveira
# Economia Brasileira

n = int(raw_input())
opiniao = map(int, raw_input().split())

count = 0
for i in range(len(opiniao)):
        if opiniao[i] == 1:
                count += 1
if count >= len(opiniao)/2.0:
        print 'N'
else:
        print 'Y'
