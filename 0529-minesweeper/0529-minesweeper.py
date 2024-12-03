class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows, cols = len(board) , len(board[0])

        q = []

        q.append((click[0] , click[1]))

        dirs = [(1,0),
                (-1,0),
                (0,1),
                (0,-1),
                (1,1),
                (-1,1),
                (1,-1),
                (-1,-1)]
        while q:
            row,col = q.pop()
            print(row,col)
            #if it's m, then 1:If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
            if board[row][col] == 'M':
                board[row][col] ='X'
                return board
            
            #if it's e: add the nei's to q?
            if board[row][col] == 'E':
                if self.mines(row,col, board,rows,cols) == 0:
                    board[row][col] ='B'
                    for direction in dirs:
                        r = row + direction[0]
                        c = col + direction[1]
                        if 0<=r and r<rows and 0<=c and c<cols:
                            q.append((r,c))
                else:
                    board[row][col] = str(self.mines(row,col, board,rows,cols))
                
        
        return board
    
    def mines(self, row, col, board,rows,cols):
        res = 0
        dirs = [(1,0),
                (-1,0),
                (0,1),
                (0,-1),
                (1,1),
                (-1,1),
                (1,-1),
                (-1,-1)]
        for directions in dirs:
            newRow = row +directions[0]
            newCol = col + directions[1]
            if 0 <= newRow < rows and 0 <= newCol < cols and board[newRow][newCol] == 'M':
                res+= 1
        return res


        