# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 2 pointer approach: we will have a left and right pointer where the space in between these 2 pointers
        # is equal to n, we want to start the left pointer at a dummy node inserted at the head of the link list 
        dummy = ListNode(0,head)
        left = dummy
        right = head 

        while n > 0 and right: #we will start the right pointer at the head and shift it until it as many spaces as n
            right = right.next
            n -= 1
        
        while right: #now that they are spaced out correctly lets just shift both until the right pointer reaches NULL
            left = left.next
            right = right.next
        
        left.next = left.next.next #we DELETE the node by removing the link and attaching it to the next one in the list
        
        return dummy.next #return the new full list except for the dummy node
