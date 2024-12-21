# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#RECURSIVE DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        # we know there is at least 1 node since the root is not empty 
        # meaning we will return 1 + the max dfs of the left side and right side

        countR = self.maxDepth(root.right)
        countL = self.maxDepth(root.left)

        # this +1 is what makes the whole problem work, since every new function call, 
        # the left child turns into the root of the new subproblem adding one once again 
        # and then searching for its children
        return 1 + max(countL, countR)
