class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        #for this, you just transpose the matrix; then reverse the rows!
        transpose = []
        rows, cols = len(matrix), len(matrix[0])
        for i in range(cols):
            transpose.append([0] * rows)
        
        for i in range(rows):
            for j in range(cols):
                transpose[j][i] = matrix[i][j]
        
        for row in transpose:
            row.reverse()
        
        for row in range(rows):
            for col in range(cols):
                matrix[row][col] = transpose[row][col]