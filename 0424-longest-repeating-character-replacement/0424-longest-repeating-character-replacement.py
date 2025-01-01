class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # ONLY UPPERCASE: 26 char
        
        # We will be using: hashmap + sliding window:
        #
        # Hashmap to store find out which is the 
        # least frequent character and see if it is replacable with 
        # our given k swaps
        #
        # L and R pointer of sliding window start at index 0:
        #
        # M = The length of our curr window minus the count of the most freq. char 
        # M must me: M <= K ( meaning we can replace the least frequent char
        #                     with the most frequent in valid k swaps)
        #
        # if M <= K is true then we expand the window by shifting the right pointer by one and ... 
        # ... we store the current max window length in Res variable
        #
        # if M >= k we shift the left pointer "shrinking" the window

        count = {} #counts freq. of each char
        res = 0 #stores the max length of a substring

        l = 0 
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0) # .get() gets the count of the current character at 
                                                # s[r] (where right pointer is) and returns its freq.
                                                # or 0 if it is currently not in the hashmap
                # M: (r-l+1) calculates len of window
                # count.values() returns every value in the hashmap
                # and max() picks the biggest value 
            while (r-l+1) - max(count.values()) > k: #makes sure the current window is valid
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res

# max(count.values()) is actually slow since it walks thorugh every value currently
# in our Hashmap and makes our algorithm O(26*n) but it is still linear time