a=1
while a>=1:
        K = int(raw_input())
        if K==0:
                a-=1
        if K>0 and K<=1000:
                N, M = map(int, raw_input().split())
                if N>-10000 and N<10000 and M>-10000 and M<10000:
                        for i in range (0, K, 1):
                                X, Y = map(int, raw_input().split())
                                if X==N or Y==M:
                                        print "divisa"
                                elif X>N and Y>M:
                                        print "NE"
                                elif X>N and Y<M:
                                        print "SE"
                                elif X<N and Y>M:
                                        print "NO"
                                elif X<N and Y<M:
                                        print "SO"
