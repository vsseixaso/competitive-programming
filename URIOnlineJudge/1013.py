a, b, c = map(int, raw_input().split())
if a > b and a > c:
	print "%d eh o maior" %a
elif b > a and b > c:
	print "%d eh o maior" %b
else:
	print "%d eh o maior" %c