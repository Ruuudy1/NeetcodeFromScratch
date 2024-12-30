# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Recursive Solution
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        #if both are empty then they are equal
        if not p and not q: 
            return True
        # if the statement above did not excecute but one is empty
        # and the other is not. 
        # we also check if the values are not equal even if not null nodes
        if not p or not q or p.val != q.val:
            return False 

        # this is the whole solution, just returns true once 
        # both subtrees end up being null at the same time 
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))