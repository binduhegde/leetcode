def find_winner(n, k):
    # players = [i for i in range(n)]
    # print(players)
    # st = 0
    # while len(players) > 1:
    #     to_pop = k%len(players)-1
    #     players.pop(to_pop- st)
    #     st += to_pop % len(players)-1
    #     print(players)
    # return players
    players = [i for i in range(n)]
    i = 0
    while len(players) > 1:
        to_pop = (k-1+i) % len(players) 
        players.pop(to_pop)
        i = to_pop
    return players[0]+1

#print(find_winner(6, 3))

#faster 
def find_winner2(n, k):
    if(n==1):
        return 0
    prevWinner = find_winner2(n-1, k)
    return (prevWinner + k) % n

print(find_winner2(3, 2))
