class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        #doesnt work, but stack implement attempt
        stack = []
        for letter in s:
          stack.append(s.count(letter))
        for letter in t:
          print(stack)
          print(t.count(letter))
          if t.count(letter) in stack:
            stack.remove(t.count(letter))
          else:
            return False
        return True
        """
        s1Arr = []
        s2Arr = []
        for i in s:
            s1Arr.append(s.index(i))
        for i in t:
            s2Arr.append(t.index(i))
        if s1Arr == s2Arr:
            return True
        return False
