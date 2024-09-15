class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #We will add elements (cars) to the stack in reverse order (aka add the rightmost car first)
        pair = [[p,s] for p,s in zip(position, speed)]  #pair up the position and speed arrays
        stack = []
        for p,s in sorted(pair)[::-1]: #sort the paired array and iterate through them in reverse order
            stack.append((target - p) / s) #calculate the time it will reach the target
            if len(stack) >= 2 and stack[-1] <= stack[-2]: #check if there is at least 2 elem in stack (as there needs to be two cars for a collission to happen) 
                #IMPORTANT: also checks if the time it takes for the second elem on the stack is greater than the head of the stack then these collide and form a car fleet
                stack.pop() #we only pop once as we are iterating in reverse order
        return len(stack) #the amount of elem left over on the stack are the fleets that are travelling independent of each other so we can return this