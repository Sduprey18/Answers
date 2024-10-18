class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #bottom row you can only move right, so lets make that first
        row =[1] * n
        for i in range(m-1):
          newRow =[1] * n
          for j in range(n-2,-1,-1):
            newRow[j] = row[j] + newRow[j + 1]
            row[j] = newRow[j]
        return row[0]
