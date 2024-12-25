# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        #recursive function that returns a bool if its balances and the height of each subtree
        def dfs(root):
        #if the root is null it is still balanced so return True for balaned and height of 0
            if not root:
                return [True,0]
            #call dfs on both subtrees
            left, right = dfs(root.left), dfs(root.right)

            # finds and checks the difference between left&right subtree is <= 1
            # Also checks if any node in the subtrees was unbalanced 
            balanced = (left[0] and right[0] and
                        abs(left[1]-right[1]) <= 1)

            #returns a pair of ifBalanced? and the height of the tree
            return [balanced, 1 + max(left[1],right[1])]
        
        #function returns a boolean so only return the 0 index which is the balanced property
        return dfs(root)[0]
