# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # cse 100  space: O(n/2 -> n) time: O(n) 
        # go through each level and make a list from left to right
        # then combine all the sublists into one list
        
        # we will do BFS (queue)
        res = []
        q = collections.deque()
        q.append(root)
        
        while q:
            qlen = len(q) # ensuring we iterate through one level at a time
            level = [] # add to our result list 
            for i in range(qlen): 
                node = q.popleft() # First in first out
                if node: 
                    level.append(node.val) # append it to the list level
                    q.append(node.left) # then append its children ->
                    q.append(node.right) # 
            if level:
                res.append(level) # add sublists to the big list
        return res
