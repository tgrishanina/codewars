def find_treasure(grid, row, col):
    # while loop: runs indefinitely until we find the treasure
    while True:
        current_value = grid[row-1][col-1]  
        if current_value == int(str(row) + str(col)):
            return current_value  
        else:
            row = int(str(current_value)[0])
            col = int(str(current_value)[1])