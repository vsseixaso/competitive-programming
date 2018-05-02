# coding: utf-8

# AA Básico 16.2 | CCC UFCG
# Vinícius Souza Seixas de Oliveira
# Round House

import math

n, a, b = map(int, raw_input().split())

if b == 0:
    print a
elif b > 0:
    pos = a + b
    while pos > n:
        pos -= n
    print pos
else:
    for i in range(abs(b)):
        a -= 1 
        if a == 0:
            a = n
    print a
