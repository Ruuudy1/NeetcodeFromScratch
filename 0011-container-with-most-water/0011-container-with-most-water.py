class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) - 1
        max_area = 0

        while left < right:
            # Calculate the current area
            h = min(heights[left], heights[right])
            w = right - left
            current_area = h * w
            
            # Update max_area if the current area is larger
            max_area = max(max_area, current_area)
            
            # Move the pointers to try to find a larger area
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area