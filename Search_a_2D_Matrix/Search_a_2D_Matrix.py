class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # define coloumns and rows
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bottom = 0, ROWS-1
        # binary search -> bottom & top
        while top < bottom:
            medianRow = (top+bottom)//2
            # greater the last integer of the medianRow
            if target > matrix[medianRow][-1]:
                top = medianRow+1
            elif target < matrix[medianRow][0]:
                bottom = medianRow-1
            else:
                break

        if not (top <= bottom):
            return False

        left, right = 0, COLS-1
        row = (top+bottom)//2
        while left <= right:
            medianCols = (left+right)//2
            if target > matrix[row][medianCols]:
                left = medianCols + 1
            elif target < matrix[row][medianCols]:
                right = medianCols-1
            else:
                return True
        return False
