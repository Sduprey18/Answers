import heapq
class Solution:
    

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # answer with heap          
        nums = [-num for num in nums]
           
        heapq.heapify(nums)
        for i in range(k):
            thing = heapq.heappop(nums)
        print(thing)
        return -thing