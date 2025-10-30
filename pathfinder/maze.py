def path_finder(maze):
    visited = set()
    maze  = maze.split("\n")
    size = len(maze) 
    endpoint = (size -1, size -1)
    
    def dfs(x, y):
        # Check if outside edges
        if x < 0 or x >= size or y < 0 or y >= size:
            return False
        # Check if wall or visited
        if maze[x][y] == 'W' or (x, y) in visited:
            return False
        # Check if solved
        if (x, y) == endpoint:
            return True
        
        visited.add((x, y))
        
        # Explore
        if dfs(x, y-1):  # S
            return True
        if dfs(x, y+1):  # N
            return True
        if dfs(x+1, y):  # E
            return True
        if dfs(x-1, y):  # W
            return True
        
        return False
    
    return dfs(0,0)
