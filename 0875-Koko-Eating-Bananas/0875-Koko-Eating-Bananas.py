class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # BRUTE FORCE: O(n*m), logic transitions smoothly to OPTIMAL SOLUTION: O(nlog(m))
         
        # This problem gives us a array of piles that is greater than or equal to p hours.
        # The K value we output is guarranteed to be between [1-max(i)] (1 since we cannot eat 0 bananas and i being the biggest pile in the array)
        # This gives us the perfect conditions to set up Binary Search:
        l, r = 1, max(piles) #set r to the biggest pile
        res = r # the max pile will always work since all piles will be eaten in the rate 1 hour each

        while l<=r:
            mid = (l+r) // 2
            currhours = 0 
            for p in piles:
                currhours += math.ceil(float(p)/mid) # round up when finding the num of hours it takes to eat a pile
            
            if currhours <= h:
                res = mid #see if res is smaller than the current mid
                r = mid-1 # now shift our right pointer to search left side
            else: 
                l = mid+1 # now shift our left pointer to search right side
        return res
