def upper_bound(vet, num):
    l, r = 0, len(vet) - 1
    while l <= r:
        mid = l + (r - l) / 2
        if vet[mid] > num:
            r = mid - 1
        else:
            l = mid + 1
    return l

n, m = map(int, raw_input().split())
n_ints = map(int, raw_input().split())
m_ints = map(int, raw_input().split())

n_ints.sort()

out = []
for i in xrange(m):
    out.append(upper_bound(n_ints, m_ints[i]))

print ' '.join(str(e) for e in out)