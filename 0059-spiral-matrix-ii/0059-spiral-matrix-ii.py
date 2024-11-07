'''
directions:
right: (0,1)
left:(0,-1)
up :(-1,0)
down : (1,0)
'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        rows = n
        cols = n
        matrix = []
        n2 = n * n
        counter = 1
        for i in range(rows):
            matrix.append([0] * cols)
        
        def dp(row,col,counter, direction):
            if counter >n2:
                print(counter)
                print("counter >n2")
                return matrix
            if row < 0 or row >= rows or col < 0 or col >= cols or matrix[row][col] != 0:
                if direction =="right":
                #then go down
                    dp(row+1,col-1,counter,'down')
                    return
                elif direction =="left":
                #then go up
                    dp(row-1,col+1,counter,'up')
                    return
                elif direction =="up":
                #then go right
                    dp(row+1,col+1,counter, 'right')
                    return
                elif direction =='down':
                    #then go left
                    dp(row-1,col-1,counter,'left')
                    return
                return
            matrix[row][col] = counter

            if direction =="right":
                dp(row,col+1,counter+1, direction)
            elif direction =="left":
                dp(row,col-1,counter+1,direction)
            elif direction =="up":
                dp(row-1,col,counter+1,direction)
            elif direction =="down":
                dp(row+1,col,counter+1,direction)
        dp(0,0,counter,'right')
        return matrix