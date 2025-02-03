# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# All this is is just BFS with a results array to return everything
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque() #initialize a queue
        q.append(root) # initialize the queue with the root node
        
        # checks if the queue is not empty and stores the length of the queue
        while q: 
            qlen = len(q)
            level = [] # make a list for each level at the time
            for i in range(qlen): 
                node = q.popleft() # first in first out
                if node: 
                    level.append(node.val) # add the curr node to the level list
                    q.append(node.left) # add the children to the queue
                    q.append(node.right) # ^
            if level:
                res.append(level) # append one level at a time on the res array to make a 2D array 
        return res
