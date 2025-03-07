# Highly optimized approach O(1) space!
# avoid having to make a copy of the matrix by storing 2 values in one int 

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ROWS = len(img)
        COLS = len(img[0])

        for r in range(ROWS):
            for c in range(COLS):
                total, cnt = 0,0

                #iterate over our 3x3 kernel
                for i in range(r-1,r+2): #range is technecally r+1 but range() func is not inclusive
                    for j in range(c-1,c+2):
                        if i< 0 or  i == ROWS or j < 0 or j == COLS:
                            continue
                        # the mod eliminates everything beefore the first 8 bits
                        total += img[i][j] % 256 
                        cnt += 1
                # since the constraint says: 0 <= img[i][j] <= 255
                # that means: 1111 1111 is the max number (8 bits)
                # aka we can store 2 values in each spot
                # one value will be in the first 8 bits the other in the bits after 
                img[r][c] = img[r][c] ^ (total // cnt) << 8

        for r in range(ROWS):
            for c in range(COLS):
                # reversing the shift left to only get the added value
                img[r][c] = img[r][c] >> 8

        return img



# NAIVE SOLUTION O(n) space:
# class Solution:
#     def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
#         ROWS = len(img)
#         COLS = len(img[0])

#         # make a 2D grid
#         res= [[0] * COLS for _ in range(ROWS)]

#         for r in range(ROWS):
#             for c in range(COLS):
#                 total, cnt = 0,0

#                 #iterate over our 3x3 kernel
#                 for i in range(r-1,r+2): #range is technecally r+1 but range() func is not inclusive
#                     for j in range(c-1,c+2):
#                         if i<0 or  i == ROWS or j < 0 or j == COLS:
#                             continue
#                         total += img[i][j]
#                         cnt += 1
#                 res[r][c] = total // cnt
#         return res