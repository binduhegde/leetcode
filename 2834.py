def min_possible_sum(n, target):
    added = 0
    for i in range(1, (min([n, int(target/2)])+1)): added += i
    for i in range(target, target+(n-(int(target/2)))): added += i
    return added
print(min_possible_sum(6, 5))

