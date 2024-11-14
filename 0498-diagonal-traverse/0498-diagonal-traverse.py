class Solution:
    def findDiagonalOrder(self, mat):
        rows, cols = len(mat), len(mat[0])
        res = []
        matSize = rows * cols

        def dp(direction, row, col):
            if len(res) == matSize:
                return

            if row < 0 or row >= rows or col < 0 or col >= cols:
                if direction == 'up':
                    if col >= cols:
                        row += 2
                        col = cols - 1
                    elif row < 0:
                        row = 0
                    direction = 'down'
                elif direction == 'down':
                    if row >= rows:
                        col += 2
                        row = rows - 1
                    elif col < 0:
                        col = 0
                    direction = 'up'
                dp(direction, row, col)
                return

            res.append(mat[row][col])

            if direction == 'up':
                dp('up', row - 1, col + 1)
            elif direction == 'down':
                dp('down', row + 1, col - 1)

        dp('up', 0, 0)
        return res
