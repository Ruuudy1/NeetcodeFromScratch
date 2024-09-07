class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = len(numbers)-1

        while l < r:
            currsum = numbers[l] + numbers[r]

            if currsum > target:   #if the sum is too big then we shift the right pointer only
                r -= 1
            elif currsum < target:  #if the sum is too small then we shift the left pointer only
                l += 1
            else:                  #if the sum is the target then we found our solution
                return [l+1, r+1]  #return the pos (the index + 1)