class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      #first intuition (probably wont work) keep sliding window of numbers, if it goes less, remove the one on the left 
      curr = nums[0]
      res = nums[0]
      for i in range(1,len(nums)):
        curr = max(nums[i], curr + nums[i])
        res = max(curr, res)
      
      return res
        