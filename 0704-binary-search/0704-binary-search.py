class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 #start 2 pointers at the start end of the array

        while l <= r: #iterate until the left and right meet or the left val crosses
            m = l + ((r-l) // 2) # this is the same thing as: m = (l+r) // 2 #calculate midway point
                                 # this way we will never have an overflow problem:
                                 # r - l: gives us the distance between the pointers
                                 # // 2 divide and truncate it by 2 to get the "halway" point of the distance between them
                                 # l + ans: by adding halway of the distance between them to l we get the midpoint val.
            match nums[m]:
                case _ if nums[m] > target:
                    r = m - 1
                case _ if nums[m] < target:
                    l = m + 1
                case _:
                    return m
        
        return -1
