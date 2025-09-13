class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      if not nums:
          return 0
      if len(nums) == 1:
          return 1
      l, r = 0, 1
    

      while r<len(nums):
        while nums[r] == nums[l]:
          nums.pop(r)
        else:
          r+= 1
          l+= 1
      
      print(nums)
      

        

      
        