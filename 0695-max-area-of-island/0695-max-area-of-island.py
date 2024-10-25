class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0

        def explore(row, col, curr):
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or grid[row][col] == "x"
                or grid[row][col] == 0
            ):
                return 0
            grid[row][col] = "x"
            curr = 1
            curr += explore(row + 1, col, curr)
            curr += explore(row - 1, col, curr)
            curr+= explore(row, col + 1, curr)
            curr+= explore(row, col - 1, curr)
            return curr

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res= max(explore(i,j,res), res)

        return res
