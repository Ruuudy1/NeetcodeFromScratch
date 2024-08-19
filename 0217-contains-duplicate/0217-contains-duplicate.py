class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # x = set(nums)
        # if len(nums) == len(x):
        #     return False
        # return True
        return len(nums) != len(set(nums))