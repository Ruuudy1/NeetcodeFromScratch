class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1   # iterate one way forward in the array
        for i in range(len(nums)):
            res[i] = prefix    # assign the prefix to every pos
            prefix *= nums[i]  # compute the prefixes as we iterate

        postfix = 1 # iterate one way BACKWARD in the array
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix   # mul the prefix and postfix
            postfix *= nums[i]  # update the postfix with the original arr val
        return res
