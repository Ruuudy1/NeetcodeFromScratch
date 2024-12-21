# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# similar solution to MaxDepth problem but with a global variable 
# to store the max height of each side
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # the self makes this a "member variable" an instance on this solution class 
        # so it can be acessible inside the nested dfs function
        self.res = 0

        #same as max depth of binary tree problem
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            # this makes it different, instead of returning the max of left and right straight away
            # we first store the current sum of the left and right tree onto the res variable
            # but since this function is recursive, this will check the max sum of the left and 
            # ... right for each node and keep the largest diameter in res
            self.res = max(self.res, left+right)
            return 1 + max(left, right)
        
        dfs(root)
        return self.res

