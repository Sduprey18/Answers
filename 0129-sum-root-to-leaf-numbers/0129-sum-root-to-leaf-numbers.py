# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
      res = []
      current = []
      def dfs(root, current):
        if not root:
          #current = []
          return
        current.append(root.val)
        #if its a leaf
        if not root.left and not root.right:
          currentString = ''.join(map(str, current))
          res.append(int(''.join(map(str, currentString))))
          
        
        dfs(root.left, current)
        dfs(root.right, current)
        current.pop()
        return 
      dfs(root, current)
      #print(res)
      print(res)
      return sum(res)

        