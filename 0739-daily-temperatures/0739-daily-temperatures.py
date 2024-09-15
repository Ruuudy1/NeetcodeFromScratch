class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Monotonic Decreasing Stack (all elements on stack will be smaller than or equal to the curr elem)
        res = [0] * len(temperatures)
        stack = [] # a pair of the temperature and its respective index

        for i,t in enumerate(temperatures):   #iterate over both temperatures (t) and indeces (i)
            while stack and t > stack[-1][0]: #check if stack empty and if the head of our stack temp is less than the curr temp
                stacktemp, stackidx = stack.pop() #pop both the head's temp and index (if curr temp is higher)
                res[stackidx] = (i - stackidx) #add to the res stack the difference between the curr index and index of the top of the stack
                #this while loop might execurte multiple times as the element after the head is popped might also be smaller than the curr elem
            stack.append([t,i]) #once the loop finishes we are guarranteed that there is no longer a smaller temperature that came before so we can append the curr temp+its index
        return res #NO NEED TO CHECK IF t IS < OR == STACK HEAD as the res is prefilled with 0's

