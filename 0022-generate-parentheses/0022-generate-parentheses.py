class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
    
    #RECURSIVE SOLUTION
        def backtracking(openN, closedN):    #if the num of open and close parentesis is equal, we found a sol
            if openN == closedN == n:        
                res.append("".join(stack))
                return
            if openN < n:        #if the num of open parenthesis is smaller than the target append another open one
                stack.append("(")
                backtracking(openN+1, closedN)
                stack.pop()
            if closedN < openN:  #if the num of closed parenthesis is less than the open, we can put a closing parenthesis
                stack.append(")")
                backtracking(openN,closedN+1)
                stack.pop()

#this will make a recursive tree like from cse101
        backtracking(0,0)
        return res