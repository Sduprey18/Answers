class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums) - 1
        res = 0
        nums.sort()
        visited = set()
        while l < r:
            if nums[l] + nums[r] == k:
                l += 1
                r -= 1
                res += 1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                r -= 1

        return res
