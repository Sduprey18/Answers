class Solution:
    def maxDepth(self, s: str) -> int:
      curr = 0
      res = 0
      for char in s:
        if char == "(":
          curr += 1
        elif char == ")":
          curr-=1 
        res = max(res, curr)
      return res