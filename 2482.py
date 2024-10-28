def create_diff(grid):
    diff = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            ones_row = len([a for a in grid[i] if a == 1])
            ones_column = len([a[j] for a in grid if a[j] == 1])
            zeros_row = len([a for a in grid[i] if a == 0])
            zeros_column = len([a[j] for a in grid if a[j] == 0])
            diff[i][j] = ones_row + ones_column - zeros_row - zeros_column
    return diff

print(create_diff([[0,1,1],[1,0,1],[0,0,1]]))
