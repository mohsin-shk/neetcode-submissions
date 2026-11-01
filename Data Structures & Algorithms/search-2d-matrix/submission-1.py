class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix), len(matrix[0])

        topR,bottomR = 0 , rows - 1
        while topR<=bottomR:
            row =  (topR + bottomR) // 2
            if matrix[row][0] > target:
                bottomR =  row - 1
            elif matrix[row][-1] < target:
                topR =  row + 1
            else:
                break
        
        if not (topR<=bottomR):
            return False
        
        row = (topR + bottomR)//2
        l,h = 0 , cols -1
        while l<=h:
            m =  (l+h)//2
            if matrix[row][m] > target:
                h = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True

        return False  