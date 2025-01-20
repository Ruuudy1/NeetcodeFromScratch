class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # python does not have a maxheap function only minheap so what we
        # we can do is iterate through and multiply every single entry in the 
        # stones list by -1 to make them negative effectively giving us a max heap
        stones = [-s for s in stones]
        heapq.heapify(stones) #O(1) operation O(n) space

        while len(stones) > 1: #only stop if there is 1 or 0 stones

            #pop twice from the heap to get the first and second largest stones
            largest, secondlargest = heapq.heappop(stones), heapq.heappop(stones)

            ###########################################################################
            ########## ALL THE MATH WILL BE BACKWARDS SINCE WE ARE WORKING ############
            ##########              WITH NEGATIVE VALUES                   ############
            ###########################################################################
            
            
            if secondlargest > largest: # we do this backwards since the stones are negative
                heapq.heappush(stones, -(secondlargest - largest)) #make the remainder negative 

        return abs(stones[0]) if stones else 0
