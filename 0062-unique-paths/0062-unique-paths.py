class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
      rows, cols = m, n
      dp = []
      for i in range(m):
        row =[]
        for j in range(n):
          row.append(0)
        dp.append(row)

      dp[0][0] = 1

      #fill first row
      for i in range(1,cols):
        dp[0][i] =  1
      
      #fill first col 
      for i in range(1,rows):
        dp[i][0] =  1
      
      #fill in the rest 
      for i in range(1,rows):
        for j in range(1,cols):
          dp[i][j] = dp[i][j-1] + dp[i-1][j]
      
      return dp[rows-1][cols-1]
        