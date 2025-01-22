# complexity log(min(n, m))

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        mid_both = total // 2 #truncates
        
        # makes sure that nums1 is the smaller of the 2 arrays
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        l,r = 0, len(nums1)-1 #set up for binary search

        while True:
            i = (l+r) // 2    #middle values of nums1
            
            # i is the index from the midpoint and we subtract 2 
            # since both arrays (nums1,nums2) start at 0
            j = mid_both - i - 2 

            # if i is out of bounds (there is an empty nums1 or nums2)
            # we can default the objects to -inf and +inf so that 
            # binary search still works correctly
            oneleft = nums1[i] if i >= 0 else float('-inf') 
            oneright = nums1[i+1] if (i+1) < len(nums1) else float('inf')
            twoleft = nums2[j] if j >= 0 else float('-inf')
            tworight = nums2[j+1] if (j+1) < len(nums2) else float('inf')

            if oneleft <= tworight and twoleft <= oneright:
                # if the total array of both is positive then the midpoint
                # is simply the median
                # odd length:
                if total % 2:
                    return min(oneright, tworight) 

                # else return the biggest elem in the left half of both 
                # arrays (1st half rightmost) 
                # + the smallest leftmost element of the right half of
                # both arrays (2nd half leftmost)
                # even length:
                return (max(oneleft,twoleft) + min(oneright, tworight)) / 2
            
            # too many elements in nums1
            elif oneleft > tworight:
                r = i-1
            # too many elements in nums2
            else: 
                l = i+1
