def deck_revealed(deck):
    sorted_deck = sorted(deck)
    ranking = [i for i in range(len(deck))]
    revealed = []
    while len(ranking) != 1:
        revealed.append(ranking[0])
        ranking.pop(0)
        ranking.append(ranking[0])
        ranking.pop(0)
    revealed.append(ranking[0])

    result = [0 for i in range(len(deck))]
    for i in range(len(revealed)):
        result[revealed[i]] = sorted_deck[i]
    print('sorted:', sorted_deck, "\nrevealed:", revealed)
    return result

print(deck_revealed([17,13,11,2,3,5,7]))
#print(deck_revealed([0,1,2,3,4,5,6,7,8,9,10,11]))
#output: = [2,13,3,11,5,17,7]