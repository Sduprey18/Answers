class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #you have to dp this :(
        rows, cols = len(grid), len(grid[0])

        dp = []
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append(0)
            dp.append(row)
        
        #starting at top left 
        dp[0][0] = grid[0][0]

        #do first row
        for i in range(1,cols):
            dp[0][i] = dp[0][i-1] + grid[0][i]

        #do first col
        for i in range(1,rows):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        #fill in the rest 
        for i in range(1, rows):
            for j in range(1, cols):
                #min for this problem cuz its min path sum
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[rows-1][cols-1]       