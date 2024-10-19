
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
          if str(sorted(word)) in hashmap:
            hashmap[str(sorted(word))] +=  [word]
          else:
            hashmap[str(sorted(word))] =  [word]
        
        res = []
        for val in hashmap.values():
          res.append(val)
        return res



