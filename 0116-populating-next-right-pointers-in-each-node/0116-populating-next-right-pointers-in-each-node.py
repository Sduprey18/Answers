"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        ogRoot = root
        if not root:
            return ogRoot
        q = []
        q.append(root)
        #q = 1
        #root = 1
        #level =[2,3]
        #for i in range 2:
        #0: 
        #
        #level = []
        node = root
        while q:
            levelLen = len(q)
            for i in range(levelLen):
                node = q.pop(0)
                if i == levelLen - 1:
                    node.next = None
                else:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
        return root
       