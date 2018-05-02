while True:
    n = int(raw_input())
    if n == 0: break
    l = map(int, raw_input().split())
    count = 0

    if len(l) == 2:
        if l[0] != l[1]: count = 2

    else:
        for i in range(len(l)):
            if i == len(l)-1:
                if (l[i] > l[0] and l[i] > l[i-1]):
                    count += 1
                elif (l[i] < l[0] and l[i] < l[i-1]):
                    count += 1
            else:
                if (l[i] > l[i+1] and l[i] > l[i-1]):
                    count += 1
                elif (l[i] < l[i+1] and l[i] < l[i-1]):
                    count += 1
    print count