def x(friends= [[]], element = []):
    for i in xrange(len(friends)):
        if (abs(element[1] - friends[i][1]) < difference):
            if(abs(element[2] - friends[i][2]) < difference):
                friends[i][0] += element[0]
                if (element[1] < friends[i][1]):
                    friends[i][1] = element[1]
                if(element[2] > friends[i][2]):
                    friends[i][2] = element[2]
                return True
    return False

nOffriends, difference = map(int, raw_input().split())

friends = []
friendsInd = []

for f in xrange(nOffriends):
    money, factor = map(int, raw_input().split())
    element = [factor, money, money]
    friendsInd.append(element)


    hasAdded = x(friends, element)

    if(not hasAdded):
        for fi in xrange(len(friendsInd) - 1):
            if (abs(friendsInd[fi][1] - element[1]) < difference):
                if(abs(friendsInd[fi][2] - element[2]) < difference):
                    element[0] += friendsInd[fi][0]

                    if(friendsInd[fi][1] < element[1]):
                        element[1] = friendsInd[fi][1]
                    if(friendsInd[fi][2] > element[2]):
                        element[2] = friendsInd[fi][2]
        friends.append(element)

print max(friends)[0]