while True:
    try:

        n, m  = map(int, raw_input().split())
        
        cont = 0
        for i in xrange(n, m+1, 1):
            x = str(i)
            y = set(x)
            if len(x) == len(y):
                cont += 1
        
        print cont
    
    except EOFError:
        break