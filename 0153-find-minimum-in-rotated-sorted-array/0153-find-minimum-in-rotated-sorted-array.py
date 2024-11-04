class Solution:
    def findMin(self, nums: List[int]) -> int:
        #almost exactly like binary search with a small twist to account for the rotation
        res = nums[0]
        l, r = 0, len(nums) -1

        while l <= r: 
            if nums[l] < nums[r]:
                res = min(res,nums[l]) #check if the res is smaller than the leftmost index

            # normal binary search
            m = (l+r) // 2
            res = min(res,nums[m])
            if nums[m] >= nums[l]:
                l = m+1
            else: 
                r = m-1
        return res