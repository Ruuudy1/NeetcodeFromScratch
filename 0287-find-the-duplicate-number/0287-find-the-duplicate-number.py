class Solution:
    #easy way to solve it will be to make a hashset and iterate through the whole arr looking for duplicates in O(n) space
    def findDuplicate(self, nums: List[int]) -> int:
        #actually stupid problem: 
        # 1. its a linked list CYCLE problem even though that is never stated in the descri.
        # 2. must solve with floyd's algorithm (slow&fast ptr: finds beginning of the cycle)
        
        # the vals in the array are pointers to other indeces in the arr
        # since the range is 1-n we never have to worry about a cycle at index 0

        slow, fast = 0, 0
        while True:          
            slow = nums[slow] 
            fast = nums[nums[fast]] #nums of fast will give us the index inside the arr (the val is an ptr) and then we will jump to that index
            if slow == fast: # walk slow and fast ptr util fast and slow meet
                break

        slow2 = 0  #now start another slow ptr at the head again and walk both slow ptr until they intersect giving us the start of the loop
        while True: #do while loop
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        return slow #returning slow or slow2 will give us the start of the cycle


#LINEAR TIME SOL: 
# space: O(n)
# time: O(1)