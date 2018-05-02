while True:
    coord = map(int, raw_input().split())
    x1 = coord[0]
    y1 = coord[1]
    x2 = coord[2]
    y2 = coord[3]

    if coord == [0, 0, 0, 0]:
        break
    elif x1 == x2 and y1 == y2:
        print 0
    elif x1 == x2 or y1 == y2:
        print 1
    elif ((x2-x1) == -(y2-y1) or -(x2-x1) == -(y2-y1) or -(x2-x1) == (y2-y1) or (x2-x1) == (y2-y1)):
        print 1
    else:
        print 2
