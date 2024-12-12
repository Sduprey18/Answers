class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            _max = max(gifts)
            
            newVal = int(sqrt(_max))

            index = gifts.index(_max)

            gifts[index] = newVal
            
            

        return sum(gifts)

        