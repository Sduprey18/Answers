class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])

        q = []

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    q.append((row, col))
                else:
                    mat[row][col] = -1

        dist = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            curr = q.pop(0)
            
            for direction in dirs:
                row = direction[0] + curr[0]
                col = direction[1] + curr[1]
                if (
                    row >= 0
                    and row < rows
                    and col >= 0
                    and col < cols
                    and mat[row][col] == -1
                ):
                    q.append((row, col))
                    #this is improtant cuz rmb mat[curr][curr] is gonna be 0 or 1 or hwatver
                    mat[row][col] = mat[curr[0]][curr[1]] + 1
                    
                    
            
        return mat