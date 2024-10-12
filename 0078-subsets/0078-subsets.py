class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
      res = [] #holds total subset
      subset = []#holds current subset
      def dfs(i):
        if i >=len(nums):#once I is over the len(nums) then you have nothing to iterate
          res.append(subset.copy())
          return 
        subset.append(nums[i])#since its subset, u will have to include curr ele
        dfs(i+1)
        subset.pop()#since its subste, you will also have to include set, without current ele
        dfs(i+1)
        return
      dfs(0)#the dfs will iterate thru itself with the dfs(i+1)
      return res
