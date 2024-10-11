class Solution:
    def minLength(self, s: str) -> int:
        #how long is ur thing supposed to run 
        #while ur string contains an AB OR a CD in it
        '''
        while "AB" in s or "CD" in s:
          if "AB" in s:
            s = s.replace("AB", "")
          if "CD" in s:
            s = s.replace("CD", "")
        return len(s)
        '''
        # stack version 
        stack = []
        for letter in s:
          if stack and stack[-1] =="A":
            if letter =="B":
              stack.pop()
            else:
              stack.append(letter)
          elif stack and stack[-1] =="C":
            if letter =="D":
              stack.pop()
            else:
              stack.append(letter)
          else:
            stack.append(letter)
        return len(stack)
          