# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #two pointer approach: one pointer at the head of the list
        dummy = ListNode() #create a dummy node to avoid null edgecases
        tail = dummy

        while list1 and list2: #are not empty:
            if list1.val < list2.val:
                tail.next = list1  #insert the smaller val onto the tail
                list1 = list1.next 
            else:
                tail.next = list2 #if list 2 is smaller insert onto tail
                list2 = list2.next 
            tail = tail.next #update tail pointe regardless of which one is bigger

        if list1: #if list 1 is null (aka there is no more vals left in the other list to compare to this one)
            tail.next = list1 #take the whole remainder of the list and append it to the end (since they are already in sorted order)
        elif list2:
            tail.next = list2 #same logic as above but for list 2
            
        return dummy.next #return the list we made except for the dummy node

