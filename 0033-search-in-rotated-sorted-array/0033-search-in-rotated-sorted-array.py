class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Since this is a sorted array that was rotated n positions, this means there \
        # is 2 sorted arrays now in this nums list. 
        #
        # Using this idea we can use BINARY SEARCH and check if the midpoint is sorted \
        # according to the left array or right array.
        #
        # **Find in which side of the rotation we are in**:
        # We will check if midpoint is less than or equal to the left value will mean  \ 
        # we are in the left portion of the array if not we are in the right portion
        #
        # After we determine what sub-array we are in, we can proceed to do Bin.Search \
        # but this time comparting the midpoint to the target value until mid  

        l = 0 
        r = len(nums) - 1

        while l <=r:
            mid = (l+r) // 2
            if target == nums[mid]:
                return mid
            
            #are we in the left portion of the array?
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else: #we are in the right sorted sub-array
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1 
                else: 
                    l = mid + 1
        return -1 # The target is not in the array