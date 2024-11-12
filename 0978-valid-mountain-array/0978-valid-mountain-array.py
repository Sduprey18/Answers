class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <3:
            return False
        wasEverIncreasing = False
        increasing = True
        decreasing = False
        for i in range(len(arr)):
            if i == 0:
                continue 
            if arr[i] == arr[i-1]:
                return False
            if increasing:
                if arr[i] >arr[i-1]:
                    wasEverIncreasing = True
                    continue
                else:
                    increasing = False
                    decreasing = True
            elif decreasing:
                if arr[i] >arr[i-1]:
                    return False
        if decreasing == False:
            return False
        if wasEverIncreasing == False:
            return False
        return True 

        