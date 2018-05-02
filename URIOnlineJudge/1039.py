import math

def distancia_de_2_pontos(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

while True:
    try:
        r1, x1, y1, r2, x2, y2 = map(int, raw_input().split())
        dist = distancia_de_2_pontos(x1, y1, x2, y2)

        if r1 >= r2+dist:
            print "RICO"
        else:
            print "MORTO"
    except EOFError: break