class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        lr, hr = 0, len(matrix) - 1
        
        goalr = -1
        
        while lr <= hr:
            
            midr = lr + (hr - lr) // 2

            if target < matrix[midr][0]:
                hr = midr - 1
            elif target > matrix[midr][-1]:
                lr = midr + 1
            else:
                goalr = midr
                break

        if goalr == -1:
            return False
        
        l, h = 0, len(matrix[goalr]) - 1
        

        while l <= h:

            mid = l + (h - l) // 2

            if target < matrix[goalr][mid]:
                h = mid - 1
            elif target > matrix[goalr][mid]:
                l = mid + 1
            else:
                return True

        return False

        