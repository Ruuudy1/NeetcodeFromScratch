class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 #left: buy and right: sell pointers
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]: # if the price went up in this day
                currProfit = prices[r] - prices[l] # calculate the amount it went up by 
                maxProfit = max(maxProfit, currProfit) #check if this curr profit is greater than our max
            else: 
                l = r # if it did not go into the prev if statement that means the right pointer is the new min of the chart so lets set our buy (left_ptr) at right's location
            r += 1 #always shift right by one regardless 
        return maxProfit