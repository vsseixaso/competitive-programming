raw_input()
array = map(int, raw_input().split())
array = set(array)
array = list(array)
array.sort()

count = 0
flag = False
for i in xrange(1, len(array), 1):
    if array[i] - array[i-1] == 1:
        count += 1
    else:
        count = 0

    if count == 2:
        flag = True
        break

if flag:
    print 'YES'
else:
    print 'NO'