n, t = map(int, raw_input().split())
vet = map(int, raw_input().split())

i = 0
j = 0
max_seq = 0
count = 0
while i < n:
    count += vet[i]
    if count > t:
        count -= vet[j]
        j += 1
    max_seq = (i - j) + 1
    i += 1

print max_seq