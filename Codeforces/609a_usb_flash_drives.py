n = int(raw_input())
m = int(raw_input())
array = []
for i in xrange(n):
    a = int(raw_input())
    array.append(a)

array.sort()
array.reverse()

count = 0
aux = 0
for i in xrange(n):
    count += 1
    aux += array[i]
    if aux >= m:
        break

print count