def find_peaks(mountain):
    op = []
    for i in range(1, len(mountain)-1):
        if mountain[i] > mountain[i-1] and mountain[i] > mountain[i+1]:
            op.append(i)
    return op