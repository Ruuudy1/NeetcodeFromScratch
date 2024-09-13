class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            match c:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(b / a))
                case _:
                    stack.append(int(c))

        return stack[0]


#SOLUTION OPTOMIZED FOR FASTER LOOKUP USING PYTHON'S "SWITCH-CASE", HERE IS PREV IF ELSE CODE IMPLEMENTATION:

# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         stack = []
#         for c in tokens:
#             if c == "+":
#                 stack.append(stack.pop() + stack.pop()) #pop the last 2 vals and append the sum back on the stack
#             elif c == "-":
#                 a, b = stack.pop(), stack.pop() #we must swap the order of the elements popped to subtract correctly
#                 stack.append(b - a)
#             elif c == "*":
#                 stack.append(stack.pop() * stack.pop()) #same as adding
#             elif c == "/":
#                 a, b = stack.pop(), stack.pop() #same as subtraction
#                 stack.append(int(b / a))
#             else:
#                 stack.append(int(c)) #if the curr val is not an operator, add the number to the stack

#         return stack[0]