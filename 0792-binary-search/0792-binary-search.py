class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
          return -1
        low, high = 0, len(nums) - 1
        while low<=high:
          mid = (low + high) // 2

          if nums[mid] == target:
            return mid
          if nums[mid] < target:
            low += 1
          if nums[mid] > target:
            high = mid - 1
        return -1