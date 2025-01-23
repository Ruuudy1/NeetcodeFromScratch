# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            # q and p are both greater than the current root
            if p.val > root.val and q.val > root.val:
                root = root.right
            # q and p are both smaller than the current root
            elif p.val < root.val and q.val < root.val:
                root = root.left
            # if root is equal to either one of q or p nodes
            else:
                return root
