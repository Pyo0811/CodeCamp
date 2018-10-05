grid =  [['.','.','.','.','.','.'],
         ['.','0','0','.','.','.'],
         ['0','0','0','0','.','.'],
         ['0','0','0','0','0','.'],
         ['.','0','0','0','0','0'],
         ['0','0','0','0','0','.'],
         ['0','0','0','0','.','.'],
         ['.','0','0','.','.','.'],
         ['.','.','.','.','.','.']]

#for i in range(len(grid)) :
#    for j in range(len(grid[i])) :
#        grid[j][8-i] = grid[i][j]

for i in range(len(grid[0])) :
    for j in range(len(grid)) :
        if j == len(grid) -1 :
            print(grid[j][i])
        else :
            print(grid[j][i], end='')
    print()
#for i in range(len(grid)) :
#    for j in range(len(grid[i])) :
#        if j == len(grid[i]) - 1 :
#            print(grid[i][j])
#        else :
#            print(grid[i][j], end='')
