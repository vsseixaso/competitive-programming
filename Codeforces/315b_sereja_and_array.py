
 n, m = map(int, raw_input().split())
ent = map(int, raw_input().split())

control = 0

for i in range(m):
        op = map(int, raw_input().split())
        if len(op) == 3:
                ent[op[1]-1] = op[2] - control
        elif op[0] == 2:
                control += op[1]
        else:
                print ent[op[1]-1] + control