class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      #notes in merck book
      rows, cols = len(grid) , len(grid[0])
      res = 0
      def explore(row,col):
        if row<0 or row>= rows or col<0 or col>=cols or grid[row][col] == 'x' or grid[row][col] =='0':
            return
        grid[row][col] = 'x'
        explore(row+1, col)
        explore(row-1, col)
        explore(row, col+1)
        explore(row, col-1)
      for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                res+= 1
                explore(i,j)
      return res


        