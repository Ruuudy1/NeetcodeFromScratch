# time: O(n)
# space: O(n)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        # double ended queue
        q = collections.deque()

        l = 0
        r = 0

        # while right pointer is in bounds 
        while r < len(nums):
            # while the queue is not empty 
            # and the rightmost val of our queue is less than the one we are inserting
            while q and nums[q[-1]] < nums [r]:
                # remove the right 
                q.pop()
            # 
            q.append(r)

            # remove the leftmost val.
            if l > q[0]:
                q.popleft()
            
            # edgecase: check that the winodow is at least size k
            if (r+1) >= k:
                # append the max value to the res array
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output