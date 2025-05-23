class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
      def visit(i, row, col):
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        rows, cols = len(board), len(board[0])

        if i == len(word):
            return True

        if row< 0 or row >=rows or col < 0 or col >=cols or board[row][col] == -1:
            return False   
            #check other rows

        temp = board[row][col]
        if board[row][col] == word[i]:
          i+= 1
          board[row][col] = -1
        else:
          return False

        for dirx, diry in directions:
                if visit(i, row + dirx,col + diry):
                    return True

        board[row][col] = temp
        return False

      rows, cols = len(board), len(board[0])

      for row in range(rows):
          for col in range(cols):
              if board[row][col] == word[0]:
                  if visit(0,row,col):
                      return True
      return False
          