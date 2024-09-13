class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: # if input is empty
            return 0 

        #two pointer approach
        l,r = 0, len(height)-1 
        lMax, rMax = height[l], height[r]  # we will keep a count of the highest amount of water seen yet on both sides
        res = 0 # sum up to return the result

        while l < r:
            if lMax < rMax:
                l += 1 
                lMax = max(lMax, height[l]) #find if the curr pos is bigger than our max
                res += lMax - height[l] #find how much water you can store in our current pos and add it to res

            else: #if right max height is bigger
                r -= 1 
                rMax = max(rMax, height[r]) #find if the curr pos is bigger than our max
                res += rMax - height[r] #find how much water you can store in our current pos and add it to res
        return res

# time O(n)
# complexity (space) O(1)



