# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, r: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
        
        if not s: 
            return True
        if not r:
            return False

        if self.sameTree(r, s):
            return True
        
        return (self.isSubtree(r.left, s) or
                self.isSubtree(r.right, s))

    def sameTree(self,r,s):
        if not r and not s:
            return True

        if s and r and r.val == s.val:
            return (self.sameTree(r.left,s.left) and
                    self.sameTree(r.right,s.right)) 
        return False
        