class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            mid_row = top + (bottom - top) // 2

            if target < matrix[mid_row][0]:
                bottom = mid_row - 1
            elif target > matrix[mid_row][-1]:
                top = mid_row + 1
            else:
                return self.search_row(matrix[mid_row], target)

        return False

    def search_row(self, row: List[int], target: int) -> bool:
        left, right = 0, len(row) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if target < row[mid]:
                right = mid - 1
            elif target > row[mid]:
                left = mid + 1
            else:
                return True

        return False

        