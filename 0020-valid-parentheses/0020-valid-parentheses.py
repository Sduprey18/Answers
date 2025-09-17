class Solution:
    def isValid(self, s: str) -> bool:
      stack = []
      for char in s:
        if char == "]":
          if not stack or stack[-1] != "[":
            return False
          stack.pop()  
        elif char == ")":
          if not stack or stack[-1] != "(":
            return False
          stack.pop()
        elif char == "}":
          if not stack or stack[-1] != "{":
            return False
          stack.pop()
        else:
          stack.append(char)
      return True if not stack else False
        
          
        