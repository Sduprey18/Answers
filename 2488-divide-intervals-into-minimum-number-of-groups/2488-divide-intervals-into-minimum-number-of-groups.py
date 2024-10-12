class Solution:
    import heapq
    def minGroups(self, intervals: List[List[int]]) -> int:
      #if there are no groups, then you return 1
      #there are only non groups if 
      #could sort then use a min heap
      intervals.sort()
      #pq = priority queue, which is just the min heap
      pq = []
      for start, end in intervals:
        if pq and pq[0] < start:
          heapq.heappop(pq)
        heapq.heappush(pq, end)
      return len(pq)

