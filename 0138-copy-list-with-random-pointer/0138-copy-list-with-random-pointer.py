"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        tocopy = { None : None} #hashmap to map every original node to its new copy IF A POINTER IS NULL MAP ITS TO NULL
        cur = head #make a pointer pointing to head 
        while cur: #walk that pointer to the end of the list until we reach the tail
            copy = Node(cur.val) #clone every node
            tocopy[cur] = copy #map the clone onto our hashmap
            cur = cur.next # walk the pointer
        #when the loop ends, we have successfully made a copy of every node but have not copied any pointers

        cur = head #remove our pointer to the start of the list
        while cur:
            copy = tocopy[cur]
            copy.next = tocopy[cur.next] #map the node in our hashmap to its pointer
            copy.random = tocopy[cur.random] #same thing with the rand pointer as the hashmap can access it in O(1)
            cur = cur.next #walk the pointer

        return tocopy[head] #return the new head of the copy
