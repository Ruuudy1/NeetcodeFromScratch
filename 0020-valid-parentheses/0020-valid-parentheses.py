class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"} #match each closing parenthesie 
        stack = []   #use a list with stack properties

        for c in s:                 #for each parenthesie in the string
            if c not in Map:    #if c is NOT a closing parenthesie
                stack.append(c) #push it to the stack 
                continue 
            if not stack or stack[-1] != Map[c]: #if empty stack or the last item doesnt match curr item
                return False
            stack.pop() #pair was succesfully matched

        return not stack #if empty stack means all pairs where successfully matched