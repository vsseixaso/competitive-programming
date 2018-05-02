from math import sqrt
n = long(raw_input())

def lovely_number(n):
    j = 1
    for i in xrange(2, int(sqrt(n))+1):
        if n % i == 0:
            j *= i
            while (n % i == 0):
                n /= i
    if n > 1:
        j *= n

    return j

print lovely_number(n)