class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solution = []

        def backtrack(path, start):
          solution.append(path[:])

          for i in range(start, len(nums)):
            #first choose
            path.append(nums[i])
            #then backtrack 
            backtrack(path,i+1)
            #then remove the curr, to get a diff combo
            path.pop()
        
        backtrack([],0)

        return solution
         