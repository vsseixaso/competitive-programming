n = int(raw_input())
l = map(int, raw_input().split())

sereja = 0
dima = 0
flag = True # True = sereja | False = dima

while len(l) > 1:
    if flag:
        if l[0] > l[-1]:
            sereja += l[0]
            l.pop(0)
        else:
            sereja += l[-1]
            l.pop(-1)

    else:
        if l[0] > l[-1]:
            dima += l[0]
            l.pop(0)
        else:
            dima += l[-1]
            l.pop(-1)

    if flag:
        flag = False
    else:
        flag = True

if flag:
    sereja += l[0]
else:
    dima += l[0]

print sereja, dima