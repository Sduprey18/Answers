# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        q=[root]

        xFound = False
        yFound = False
        xParent = None
        yParent = None
        while q:
            #print("while doing" , q)

            #go level by level
            for i in range(len(q)):
                node = q.pop(0)
                print(xFound, yFound)
                if node.val == x:
                    xFound = True
                if node.val == y:
                    yFound = True
                if xFound and yFound:
                    return True
                if node.left:
                    if node.left.val == x:
                        xParent = node.val
                    if node.left.val == y:
                        yParent = node.val
                    q.append(node.left)
                if node.right:
                    if node.right.val == x:
                        xParent = node.val
                    if node.right.val == y:
                        yParent = node.val
                    q.append(node.right)
                if xParent == yParent:
                    print(xParent, yParent)
                    print('doing parent')
                    if xParent:
                        return False
            if xFound ^ yFound:
                print("this")
                return False
                
        return False