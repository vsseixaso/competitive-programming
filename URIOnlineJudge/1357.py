br = [
[ ".*", "*.", "*.", "**", "**", "*.", "**", "**", "*.", ".*" ],
[ "**", "..", "*.", "..", ".*", ".*", "*.", "**", "**", "*." ],
[ "..", "..", "..", "..", "..", "..", "..", "..", "..", ".." ]]


while True:
        saidabr = [[],[],[]]
        n = int(raw_input())
        if n == 0: break

        op = raw_input()
        if op == 'S':
                s = raw_input()
                for i in range(n):   
                        pos = int(s[i])
                        for j in range(3):
                                saidabr[j].append(br[j][pos])
                for i in range(3): 
                        out = ''
                        for j in range(len(saidabr[0])):
                                out += str(saidabr[i][j])
                                if j != n-1: out += ' '
                        print out

        else:
                b = []
                for i in range(3):
                        ent = raw_input().split()   
                        b.append(ent)

                saidanum = ''
                for i in range(len(b[0])):
                        aux1 = b[0][i]+b[1][i]+b[2][i]
                        for j in range(len(br[0])):
                                aux2 = br[0][j]+br[1][j]+br[2][j]
                                if aux1 == aux2:
                                        saidanum += str(j)
                print saidanum