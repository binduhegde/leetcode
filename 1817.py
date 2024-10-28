def active_minutes(logs, k):
    count = {}
    for i in logs:
        if i[0] in count:
            if i[1] not in count[i[0]]: count[i[0]].append(i[1])
            else: continue
        else:
            count[i[0]] = [i[1]]
    for key, v in count.items():
        count[key] = len(v)
    
    freq = {}
    for i in count.values():
        freq[i] = freq.get(i, 0)+1
    
    output = []
    for i in range(k):
        if i + 1 in freq:
            output.append(freq[i+1])
        else:
            output.append(0)
    return output

print(active_minutes([[0,5],[1,2],[0,2],[0,5],[1,3]], 5))
