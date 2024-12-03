class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #create and populate freqmap
        freqMap = {}
        for letter in magazine:
            if letter not in freqMap:
                freqMap[letter] = 0
            freqMap[letter] += 1
        
        #take away from freqmap now, if anything goes below 0 return false
        for letter in ransomNote:
            if letter not in freqMap:
                return False
            freqMap[letter] -=1 
            if freqMap[letter] ==0:
                del freqMap[letter]
        return True 

        