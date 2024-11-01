class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        res = []
        for word in strs:
            sortedWord = sorted(word)
            sortedWord = str(sortedWord)
            if sortedWord in hashmap:
                hashmap[sortedWord].append(word)
            else:
                hashmap[sortedWord] = [word]
        
        for key, value in hashmap.items():
            res.append(value)
        
        return res
