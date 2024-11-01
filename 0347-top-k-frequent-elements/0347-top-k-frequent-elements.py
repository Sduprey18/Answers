class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for num in nums:
            if num in freqMap:
                freqMap[num] += 1 
            else:
                freqMap[num] = 1 
        output = []
        for i in range(k):
            
            largest_key = max(freqMap, key=freqMap.get)
            output.append(largest_key)
            del freqMap[largest_key]
        return output

            
        
            
        
      