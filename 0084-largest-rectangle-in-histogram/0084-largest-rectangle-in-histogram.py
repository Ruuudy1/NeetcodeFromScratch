class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # we will store each histogram as a pair: (index, height)

        for i,h in enumerate(heights):
            start = i  #start at the pos the histogram is found (we will need to consider the prev indeces in the next iterations)
            while stack and stack[-1][1] > h: # while stack is not empty AND the head of the stack's height is greater than the height we just reached
                index, height = stack.pop() #pop the whole pair: (index, height) since the next height is bigger
                maxArea = max(maxArea, height * (i-index)) #check if the possible rectangle we just popped is bigger than our curr maxArea
                start = index
            stack.append((start,h)) # change the start index and push the new pair onto the stack
        
        for i,h in stack: #now we will iterate to see if there is any leftover pairs on the stack (aka a pair whos max width is the up to the last elem on the heights arr)
            maxArea = max(maxArea, h * (len(heights) - i)) # height is on the stack and the width will be the whole len of the histogram from the start index
        return maxArea 

#hardest problem yet
#runtime: O(n) (only push and pop each elem once)
#space: O(n) (stack)