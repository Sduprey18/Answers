class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        stack = [0] * n
        for i in range(len(flowerbed)):
            if not stack:
                break
            if len(flowerbed) == 1:
                if flowerbed[i] == 0:
                    stack.pop()
                break

            if flowerbed[i] == 0 and i == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                stack.pop()
                continue 
            if flowerbed[i] == 0 and i == len(flowerbed) - 1 and flowerbed[i-1] == 0:
                flowerbed[i] = 1
                stack.pop()
                continue
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] ==0:
                flowerbed[i] = 1
                stack.pop()
                continue
        return len(stack) == 0