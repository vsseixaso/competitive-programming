def euclides_mdc(x, y):
    while y != 0:
        temp = y
        y = x % y
        x = temp
    return x

n = int(raw_input())
for i in range(n):
    x, y = map(int, raw_input().split())
    print euclides_mdc(x, y)