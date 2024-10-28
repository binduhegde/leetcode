def generate(n):
    if n == 1: return [[1]]
    triangle = [[1], [1,1]]
    for i in range(2, n):
        prev = triangle[-1]
        el = [1]
        for j in range(len(prev)//2 ):
            el.append(prev[j]+ prev[j+1])
        el = el+el[:len(prev)//2][::-1] if len(prev) % 2 == 0 else el+el[::-1]
        triangle.append(el)
    return triangle

print(generate(7))