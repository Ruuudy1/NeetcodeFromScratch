class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #since the 2D array (matrix) is already sorted, the only thing we need to do Is run binary search twice to get a:
        # O(log(n) + log(m)) time solution
         
        #no checks for non empty since problem says matrix is never empty
        row = len(matrix)
        col = len(matrix[0])
        head, tail = 0, row - 1

        while head <= tail:
            row = (head + tail) // 2 #get the middle row of the matrix first 
            if target > matrix[row][-1]:  # check if the target val is greater than the largest val (since [-1]) of the middle row
                head = row + 1   # look at one row below this row 
            elif target < matrix[row][0]: # target val is less than the smallest val (since [0]) in this middle row 
                tail = row - 1   # look at one row above this row 
            else:
                break # the target value is inside this row

        if not (head <= tail): # if target does not exist in our matrix
            return False
        
        #now time for binary search
        row = (head + tail) // 2
        l, r = 0, col - 1 # initialize l r pointers

        while l<=r: # Binary Search
            m = (l+r) // 2
            if target > matrix[row][m]:
                l = m + 1 
            elif target < matrix[row][m]:
                r = m - 1
            else: 
                return True 
        return False