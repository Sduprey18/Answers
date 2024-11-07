class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #how would we do this iteratively, def use while loop
        maxSize = len(matrix) * len(matrix[0])
        print(f"the len of this is {maxSize}")
        row, col = 0, 0
        res= []
        
        rightWall = len(matrix[0])
        downWall = len(matrix)
        leftWall = -1
        upWall = 0
        direction = 'right'
        while len(res) != maxSize:
            if direction == "right":
                while col<rightWall:
                    res.append(matrix[row][col])
                    col += 1
                #go down 1
                row += 1
                col -= 1
                rightWall -=1
                direction = 'down' 
            elif direction == "down":
                while row<downWall:
                    res.append(matrix[row][col])
                    row += 1
                #go up 1
                row -= 1
                col -=1
                downWall -=1
                direction = 'left'
            elif direction == "left":
                while col>leftWall:
                    res.append(matrix[row][col])
                    col -= 1
                #go left 1
                row -= 1
                col +=1
                leftWall +=1
                direction = 'up'
            elif direction == "up":
                while row>upWall:
                    res.append(matrix[row][col])
                    row -= 1
                #go left 1
                row += 1
                col +=1
                upWall +=1
                direction = 'right'
        return res
            