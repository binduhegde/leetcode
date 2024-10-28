def find_city(paths):

    position = {}
    for path in paths:
        for i in range(2):
            if path[i] in position and i not in position[path[i]]:
                position[path[i]].append(i)
            elif path[i] not in position:
                position[path[i]] = [i]

    for key, value in position.items():
        if len(value) == 2:
            continue
        elif value[0] == 1:
            return key



print(find_city([["B","C"],["D","B"],["C","A"],["B", "A"]]))