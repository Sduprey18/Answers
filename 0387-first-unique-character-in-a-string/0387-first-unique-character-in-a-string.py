class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}

        for i in range(len(s)):
           
            if s[i] not in counter:
                counter[s[i]] = i
            elif s[i] in counter:
                
                counter[s[i]] = -1

        _min = float('inf')
        

        for key, value in counter.items():
        
            if value != -1:
                _min = min(_min, value)

        if _min == float('inf'):
            return -1
        
        
        return _min