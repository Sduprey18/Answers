import heapq
class Solution:
    

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # answer with heap     
        #since its max-heap, we have to make vals neg     
        nums = [-num for num in nums]
           
        heapq.heapify(nums)
        for i in range(k):
            thing = heapq.heappop(nums)
        print(thing)
        #remember, since u had to make it neg to make maxheap, u need to neg it to get reg val again
        return -thing