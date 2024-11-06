class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      nums = set(nums)
      longest = 0
      res =0 
      for num in nums:
        if num - 1 not in nums:
            longest = 0
            while num+longest in nums:
                longest += 1
                res = max(longest,res)
      return res
        