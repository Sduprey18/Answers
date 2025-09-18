# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
      counter = {}

      def dfs(node):
        if not node:
          return 
        
        if node.val not in counter:
          counter[node.val] = 1
        else:
          counter[node.val] += 1
        
        dfs(node.left)
        dfs(node.right)

      dfs(root)
      _max = max(counter.values())
      res =[]
      for key, value in counter.items():
        if value == _max:
          res.append(key)

      return res