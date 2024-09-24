# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #fast and slow pointer approach: if we start a slow pointer at head and a fast pointer at the next node:
        #when fast reaches NULL, slow's next node will be the middle of the list
        slow, fast = head, head.next
        while fast and fast.next: #make sure fast's curr pos and its next pos is not null (since it moves by 2)
            slow = slow.next
            fast = fast.next.next
            #once this loops ends we are guarranteed to have found the tail and the middle of the list 
        second = slow.next
        prev = slow.next = None #set both slow.next and declare a prev variable to NULL

        while second: #REVERSE THE SECOND HALF OF THE LIST: temp variable to flip the node's pointer
            temp = second.next 
            second.next = prev
            prev = second 
            second = temp
        
        #MERGE BOTH HALFS OF THE LIST NOW
        first, second = head, prev 
        while second: 
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
        #NO NEED TO RETURN 
