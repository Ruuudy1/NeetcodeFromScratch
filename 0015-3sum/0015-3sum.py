class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() #since they are in acending order, we only need to loop over the first val and then do TwoSumII on the remainder

        for i,a in enumerate(nums): #iterate over index and val to avoid duplicates
            if a > 0:
                break
            if i>0 and a == nums[i-1]:
                continue #skip over value if the next index's val is the same as the previous'

            # NOW WE CAN COPY AND PASTE THE SAME SOLUTION FROM TWOSUM II:
            l,r = i+1, len(nums)-1 #establish left and right pointer
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:   #if equal
                    res.append([a,nums[l],nums[r]])
                    l += 1 
                    r -= 1
                    while nums[l] == nums[l-1] and l<r: #mini while loop to make sure we do not get duplicate vals
                        l += 1
        return res

