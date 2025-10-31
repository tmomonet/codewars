import java.util.HashSet;
import java.util.List;

public class Finder {
    
    static boolean pathFinder(String maze) {
      HashSet<List<Integer>> visited = new HashSet<>();
      
      String[] mazeArray = maze.split("\n");
      
      int size  = mazeArray.length;
      
      return dfs(0, 0, size, mazeArray, visited);
    }
  
    private static boolean dfs (int x, int y, int size, String[]maze, HashSet<List<Integer>> visited){
        if (x < 0 || x >= size || y < 0 || y >= size){
          return false;
        }
        
        if (maze[y].charAt(x) == 'W' || visited.contains(List.of(x, y))){
          return false;
        }
        
        if (x == size -1 && y == size - 1) {
          return true;
        }
        
        visited.add(List.of(x, y));
      
        if (dfs(x, y - 1, size, maze, visited)){
          return true;
        }
        
        if (dfs(x, y + 1, size, maze, visited)){
          return true;
        }
      
        if (dfs(x + 1, y, size, maze, visited)){
          return true;
        }
      
        if (dfs(x - 1, y, size, maze, visited)){
          return true;
        }
      
        return false;
      }
}
