class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ROWS = len(img)
        COLS = len(img[0])

        # make a 2D grid
        res= [[0] * COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                total, cnt = 0,0

                #iterate over our 3x3 kernel
                for i in range(r-1,r+2): #range is technecally r+1 but range() func is not inclusive
                    for j in range(c-1,c+2):
                        if i<0 or  i == ROWS or j < 0 or j == COLS:
                            continue
                        total += img[i][j]
                        cnt += 1
                res[r][c] = total // cnt
        return res
