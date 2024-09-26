def has_exit(maze):
    count_k = ''.join(maze).count('k')
    if count_k > 1:
        raise InvalidMazeError("There should be no multiple Kates")
    
    # Check if there's a 'k' in the maze
    if count_k == 0:
        return False

    # Locate the position of 'k'
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'k':
                start_pos = (i, j)
                break

    # Check if 'k' can move to the edge of the maze
    rows = len(maze)
    cols = len(maze[0])

    # Directions for up, down, left, right movements
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # BFS or DFS function to explore the maze
    def can_escape(x, y, visited):
        # Check if we are at the outer wall
        if x == 0 or x == rows - 1 or y == 0 or y == cols - 1:
            return True
        
        # Mark this cell as visited
        visited.add((x, y))
        
        # Explore all directions
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            # Check boundaries and if the next cell is a space
            if 0 <= new_x < rows and 0 <= new_y < cols:
                if (new_x, new_y) not in visited and maze[new_x][new_y] == ' ':
                    if can_escape(new_x, new_y, visited):
                        return True

        return False

    # Start searching from the position of 'k'
    visited = set()
    return can_escape(start_pos[0], start_pos[1], visited)