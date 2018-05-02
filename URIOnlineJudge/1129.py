opcoes = ['A', 'B', 'C', 'D', 'E']

while True:
    n = int(raw_input())
    if n == 0:
        break

    for i in xrange(n):
        linha = map(int, raw_input().split())
        controller = []
        for j in xrange(5):
            if linha[j] <= 127:
                controller.append(opcoes[j])

        if len(controller) != 1:
            print '*'
        else:
            print controller[0]