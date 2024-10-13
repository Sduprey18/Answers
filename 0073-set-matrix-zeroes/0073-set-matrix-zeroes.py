class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        truthRow = [False] * rows
        truthCol = [False] * cols
        for i in range(len(matrix)):
          for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
               truthRow[i] = True
               truthCol[j] = True
        
        for i in range(rows):
          for j in range(cols):
            if truthRow[i] or truthCol[j]:
              matrix[i][j] =0

