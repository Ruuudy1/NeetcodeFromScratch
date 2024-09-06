class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # O(n^2) aka O(9^2) since size of sudoku board must be 9x9

        cols = collections.defaultdict(set)  #hash set for each row, col, and 3x3 grid
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9): #walk through every pos in the board
                if board[r][c] == ".":
                    continue #if empty val skip it
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3)]):
                    #if the curr num inside the row/3x3/col has already 
                    #been seen means it contains a duplicate
                    #we check what square we are in by dividing and TRUNCATING the row and col
                    return False
                #if not in the hashsets add them for next iteration
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True #if we exit iterate through the whole 9x9 successfully