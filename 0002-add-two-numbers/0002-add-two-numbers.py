# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#                                                                                                1 
#why is this a good problem: it brings back the fundamentals of summing two large numbers ex:   135
#                                                                                             + 125
#                                                                                            --------
#                                                                                               260
# since the list are given in reverse order we can easily add the 2 first values (ones, tens, hundreds place) 
# and make a new node with the result we just need to remember to carry the 1 (edge case)  

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # make a dummy node as our pointer to iterate through the list (avoiding edge cases of inserting if the list was empty)
        curr = dummy 

        carry = 0 # if v1 + v2 > 10: we will carry the 1
        while l1 or l2 or carry: #iterate through both lists while they are not empty (if our carry is not empty also continue)
            v1 = l1.val if l1 else 0 
            v2 = l2.val if l2 else 0 #retrieve the val from both lists, if one list is null the val retrieved is 0

            val = v1 + v2 + carry #add the digits together 
            carry = val // 10
            val = val % 10 #determine if there is any carry (if no remainder mod will be 0 so no need to check if remainder is 0)
            curr.next = ListNode(val) #make a new node with this value we calculated

            #walk the pointers:
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next #return our new list excluding our temp dummy node
