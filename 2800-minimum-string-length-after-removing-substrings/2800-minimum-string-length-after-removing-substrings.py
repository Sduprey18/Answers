class Solution:
    def minLength(self, s: str) -> int:
        #how long is ur thing supposed to run 
        #while ur string contains an AB OR a CD in it
        while "AB" in s or "CD" in s:
          if "AB" in s:
            s = s.replace("AB", "")
          if "CD" in s:
            s = s.replace("CD", "")
        return len(s)
