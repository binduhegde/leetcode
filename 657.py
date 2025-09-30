# my way. If number of Ups and Downs are equal and
# the number of left and rights are equal, then return True
def judgeCircle(moves: str) -> bool:
    freq = {'U': 0, 'D': 0, 'L': 0, 'R': 0}

    for move in moves:
        freq[move] += 1

    return freq['U'] == freq['D'] and freq['L'] == freq['R']


# faster and shorter
def judgeCircle2(moves: str) -> bool:
    return moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D")
