n, t = map(int, raw_input().split())
queue = list(raw_input())

for j in xrange(t):
	i = 0
	while(i < n-1):
		if (queue[i] == "B" and queue[i+1] == "G"):
			queue[i], queue[i+1] = queue[i+1], queue[i]
			i+=1
		i+=1

print "".join(str(x) for x in queue)