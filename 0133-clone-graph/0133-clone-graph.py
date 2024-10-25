"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtoNew = {}
        def clone(node):
          if node in oldtoNew:
            return oldtoNew[node]
          headNode = Node(node.val)
          oldtoNew[node] = headNode
          for neighbor in node.neighbors:
            headNode.neighbors.append(clone(neighbor))
          return headNode
        return clone(node) if node else None