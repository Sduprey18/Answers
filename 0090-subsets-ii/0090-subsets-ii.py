class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans, curr = [], []
        nums.sort()
        def backtrack(start):
            print(curr)
            if curr not in ans:
                ans.append(curr[:])      
            for i in range(start, len(nums)):
            # Skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue
                curr.append(nums[i])
                backtrack(i + 1)
                curr.pop()

        backtrack(0)
        return ans
