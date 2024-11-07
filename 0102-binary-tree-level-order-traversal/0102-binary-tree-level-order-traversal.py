# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      #ok, so you want to create an array to keep all the nodes youre up to, until youre done
      #you use the levelOn to append to ur sub array, since the value u return has to be arrays in an array
      res =[]
      if root is None:
        return res
      queue = [root]
      while queue:
        levelOn = len(queue)
        level = []
        for i in range(levelOn):
          node = queue.pop(0)
          if node:
            level.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        if level:
          res.append(level)

      return res