q, e = map(int, raw_input().split())
list_e = map(int, raw_input().split())

list_q=[]

for i in range(q):
        a = int(raw_input())
        if a in list_q:
                print 0 
        else:
                list_q.append(a)
                if a in list_e:
                        print 0
                else:
                        print 1