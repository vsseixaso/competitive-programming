N = int(raw_input())

a = N / 365
m = N % 365 / 30
d = N % 365 % 30

print "%d ano(s)" %a
print "%d mes(es)" %m
print "%d dia(s)" %d