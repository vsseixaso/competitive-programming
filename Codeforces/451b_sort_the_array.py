def isOrdered (a):
	for i in xrange(1,len(a)):
		if (a[i-1] > a[i]):
			return False
			break

	return True

def invert(a):
	aux = a[:front]
	for i in xrange(end, front-1, -1):
		aux.append(a[i])
	if (len(aux) < len(a)):
		aux += a[len(aux):]
	
	return aux

n = int(raw_input())
array = map(int, raw_input().split(" "))

front = 0
end = 0
for i in xrange(1,n):
	if array[i-1] > array[i]:
		front = i-1
		break

end = front;

while end < n-1 and array[end] > array[end + 1]:
	end+=1

array = invert(array)

if (isOrdered(array)):
	print "yes\n%d %d" %(front+1, end+1)
else:
	print "no"