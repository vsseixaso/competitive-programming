# coding: utf-8

n = int(raw_input())
for i in xrange(n):
    texto = raw_input()
    mid = len(texto)/2
    p1 = mid-1
    p2 = len(texto)-1
    
    ans=''
    while p1>=0:
        ans+=texto[p1]
        p1-=1
    while p2>=mid:
        ans+=texto[p2]
        p2-=1
    
    print ans