class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(path, index):
          res.append(path[:])

          for i in range(index,len(nums)):

            if i>index and nums[i] == nums[i-1]:
              continue 
            #first choose to add
            path.append(nums[i])

            #then choose to backtrack
            backtrack(path,i+1)

            #then pop for all combos 
            path.pop()
        
        backtrack([],0)
        
        return res
