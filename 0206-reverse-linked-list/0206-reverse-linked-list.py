# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #iterative sol: time: O(n), space: O(1)

        prev, curr = None, head #two pointer approach, one prev node and one at head

        while curr: #while the curr isnt NULL
            temp = curr.next #temporary variable to store the link to the next node
            curr.next = prev #point next pointer to the previous node
            prev = curr #assign the prev node to curr
            curr = temp #make the curr the next node on the list now and repeat the process
        return prev #which is now the head of the list