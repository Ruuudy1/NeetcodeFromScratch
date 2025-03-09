# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# this is the continuation of a leetcode easy problem "Merge 2 Sorted Lists"
# we can divide and conquer and break this problem down into the "Merge 2 Sorted Lists" problem
# reducing the runtime from O(n*k) to O(nlogk) by dividing 
# n: the number of lists 
# k: the number of times we have to go through each merged list
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not list or len(lists) == 0:
            return None
        
        # take pairs of linked lists and merge them 
        # until there is only one big linkedList
        while len(lists) > 1:
            # make a new list for the merged list
            mergedLists = []

            # pairs of lists so the incremented is 2
            for i in range(0, len(lists), 2):
                
                # pass in the first node of the 2 lists
                # safety check to see if l2 is not outofbounds
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                #merge them
                mergedLists.append(self.mergeTwoLists(l1,l2))
            #append the merged list
            lists = mergedLists
        #return the merged list ( in the first index )
        return lists[0]
    

    #this is a LeetCode Easy problem ( Merge Two Sorted Lists )
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy 

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next

