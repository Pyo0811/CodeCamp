def print_table(input_table):
    col_widths = []
    for i in range(len(input_table)):
        col_widths.append(0)
        for j in range(len(input_table[i])):
            print(col_widths[i])
            if col_widths[i] < len(input_table[i][j]):
                col_widths[i] = len(input_table[i][j])
    for i in range(len(table_data[0])) :
        for j in range(len(table_data)) :
            print(table_data[j][i].rjust(col_widths[j]) + ' ', end='')
        print()
    #print(col_widths)

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)
