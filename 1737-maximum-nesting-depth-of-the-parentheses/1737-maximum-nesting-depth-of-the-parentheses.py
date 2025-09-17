class Solution:
    def maxDepth(self, s: str) -> int:
        #for this, we probably want to use a stack. im thinking we would want to maybe just keep a cmounter for every time we pop?
        stack = []
        curr = 0
        res = 0
        for char in s:
          if stack:
            if char == ")":
              curr = len(stack)
              res = max(curr, res)
              stack.pop()
            else:
              if char == "(":
                stack.append(char)
          else:
            if char == "(":
              stack.append(char)
        return res
