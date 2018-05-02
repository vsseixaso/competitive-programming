while True:
    try:
        def fatorial(x):
            if x <= 1:
                return 1
            return x*fatorial(x-1)

        n, m = map(int, raw_input().split())
        print fatorial(n) + fatorial(m)
    except EOFError: break