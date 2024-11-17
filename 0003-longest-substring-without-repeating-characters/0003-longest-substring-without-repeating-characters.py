class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #SLIDING WINDOW (keep a subarray/window that removes a character from the left as soon as it repeats on the rightmost)
        #runtime: O(n) space/complexity: O(n)

        chars = set()
        l = 0 
        res = 0

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            res = max(res, (r-l)+1)
        return res