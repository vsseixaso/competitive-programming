while True:
    players, square = map(int, raw_input().split())
    if players == square == 0: break
    traps = map(int, raw_input().split())
    n = int(raw_input())

    positions = [0] * players
    can_play = [True] * players

    cont = 0
    pott = 0
    i = 0
    while i < n:
        pott = cont % players

        if can_play[pott]:
            d1, d2 = map(int, raw_input().split())
            positions[pott] += d1 + d2
            if positions[pott] in traps:
                can_play[pott] = False
        else:
            can_play[pott] = True
            i -= 1

        cont += 1
        i += 1

    print pott + 1