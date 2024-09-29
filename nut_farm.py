def shake_tree(tree):
    # Initialize the landing positions count
    height = len(tree)
    width = len(tree[0])
    nut_positions = [0] * width
    
    # Iterate over the top row to find all nut positions
    for i in range(width):
        if tree[0][i] == 'o':  # Found a nut
            col = i  # Start from the nut's column
            stuck = False  # Track if the nut gets stuck
            
            # Traverse each row and adjust the nut's position
            for row in range(1, height):
                if tree[row][col] == '/':
                    if col > 0:  # Move left, but not out of bounds
                        col -= 1
                elif tree[row][col] == '\\':
                    if col < width - 1:  # Move right, but not out of bounds
                        col += 1
                elif tree[row][col] == '_':
                    stuck = True  # Nut gets stuck, mark it
                    break  # Stop tracking this nut
                
                # Continue falling for '.', '|', or empty spaces
            
            # If the nut did not get stuck, increment its final landing position
            if not stuck:
                nut_positions[col] += 1
    
    return nut_positions