s = raw_input()

l = []
for i in xrange(len(s)):
    l.append(s[i])
l.sort()

array = [1]
count = 0
for i in xrange(1, len(l), 1):
        if l[i] == l[i-1]:
            array[count] += 1
        else:
            count += 1
            array.append(1)

count = 0
for i in xrange(len(array)):
    if array[i] % 2 != 0:
        count += 1

if count <= 1:
    print "First"
else:
    if count % 2 == 1:
        print "First"
    else:
        print "Second"