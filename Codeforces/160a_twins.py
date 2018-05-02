def cumulative_sum(array):
    out = [array[0]]
    for i in xrange(1, len(array), 1):
        out.append(array[i] + out[i-1])

    return out

trash = raw_input()
array1 = map(int, raw_input().split())

if len(array1) == 1:
    print 1
elif len(array1) == 2:
    if array1[0] != array1[1]:
        print 1
    else:
        print 2
else:
    array1.sort()
    array2 = cumulative_sum(array1)

    ref = array2[-1]
    aux = 0
    for i in xrange(len(array2)-2, -1, -1):
        if (ref - array2[i]) > array2[i]:
            aux = i + 1
            break

    print len(array2) - aux