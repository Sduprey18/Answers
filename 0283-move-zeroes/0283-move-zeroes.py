class Solution(object):
    def moveZeroes(self, nums):
        numsL = len(nums)
        j = 0
        for i in range (0, numsL):
            if(nums[i] != 0):
                nums [i], nums[j] = nums[j], nums [i]
                j += 1
            
        
        
        
       