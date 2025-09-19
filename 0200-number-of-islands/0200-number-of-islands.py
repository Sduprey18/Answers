class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      #lets cook this
      rows, cols = len(grid), len(grid[0])

      visited = []
      for row in range(rows):
        rowHolder = []
        for col in range(cols):
          rowHolder.append(False)
        visited.append(rowHolder)
      
      def bfs(start):
        r, c = start
        q = []
        q.append((r,c))
        visited[r][c] = True 
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    
        while q:
          r, c = q.pop(0)

          for _dir in dirs:
            nr, nc = _dir[0] + r, _dir[1] + c

            if (0<=nr<rows and 
                0<=nc<cols and
                 not visited[nr][nc] and 
                 grid[nr][nc] == "1"):
                 visited[nr][nc] = True 
                 q.append((nr,nc))
      
      res =0 

      for row in range(rows):
        for col in range(cols):
          if grid[row][col] == "1" and not visited[row][col]:
            res += 1 
            bfs((row,col))
      
      return res 


        