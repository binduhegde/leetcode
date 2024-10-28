def sort_people(names, heights):
    return[name for _, name in sorted(zip(heights, names), reverse = True)]

print(sort_people(["Mary","John","Emma"], [180,165,170]))
print(sort_people(["Alice","Bob","Bob"],[155,185,150]))