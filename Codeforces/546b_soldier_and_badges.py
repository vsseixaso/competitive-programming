n = int(raw_input())
a = map(int, raw_input().split())
a.sort()

count = 0

for i in range(len(a) - 1):
	while a[i + 1] <= a[i]:
		a[i + 1] += 1
		count += 1

print count