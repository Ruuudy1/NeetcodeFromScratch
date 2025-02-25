from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: 
            return "" # edge case

        target_count = Counter(t) # the required frequencies of subset t 
        window_count = Counter()

        # start both left and right pointer at 0 and expand r until the freq of this 
        # substring matches t 
        # then we will shirnk l and see if we still satisfy the condition 
        # return the smallest valid window
        l, r = 0, 0  
        min_len = float("inf")
        min_window = ""
        required_chars = len(target_count)
        formed_chars = 0

        while r < len(s):
            char = s[r]
            window_count[char] += 1

            if char in target_count and window_count[char] == target_count[char]:
                formed_chars += 1
            
            while formed_chars == required_chars:  # Valid window
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_window = s[l:r + 1]


                window_count[s[l]] -= 1 
                if s[l] in target_count and window_count[s[l]] < target_count[s[l]]:
                    formed_chars -= 1
                
                l += 1  # Shrink from the left

            r += 1  # Expand the right

        return min_window
