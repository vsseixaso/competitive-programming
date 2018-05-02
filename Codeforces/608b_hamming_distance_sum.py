ms = raw_input()
ns = raw_input()

n = len(ns)
m = len(ms)

win = n-m+1
win1 = ns[:win].count("1")
ans = 0

for i in xrange(m):
    if ms[i]=="1":
        ans += (win-win1)
    else:
        ans += win1

    if ns[i]=="1":
        win1-=1
    if i+win < n:
        if ns[i+win]=="1":
            
            win1+=1
print ans