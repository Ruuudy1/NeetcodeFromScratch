class Solution:
    def isPalindrome(self, s: str) -> bool: 

        s = s.lower()

        left = 0
        right = len(s) - 1

        isPalindrome = True

        while left < right:
            if not self.ascii(s[left]): #self means referencing a method inside the same class
                left += 1
                continue
            if not self.ascii(s[right]):
                right -= 1
                continue
            if s[left] != s[right]:
                isPalindrome = False
                break
            left += 1
            right -= 1
        return isPalindrome
    
    def ascii(self, ptr:str) -> bool:
        return (48 <= ord(ptr) <= 57) or (65 <= ord(ptr) <= 90) or (97 <= ord(ptr) <= 122)
