class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if nums[i] + nums[j] == target and i != j:
        #             return [i,j]

        hashmap = {} # key=index, value=arr_val
        for i,n in enumerate(nums): # i=index, n=arr_val
            complement = target - n 
            if complement in hashmap: #hash-lookup the difference from target
                return [hashmap[complement], i] # hashlookup (aka previously found), curr_index
            hashmap[n] = i #else append that new index to hashmap 

