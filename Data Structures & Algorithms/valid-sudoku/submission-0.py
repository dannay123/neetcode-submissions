from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column = defaultdict(set)
        row = defaultdict(set)
        square = defaultdict(set)
        for r in range(0, len(board)):
            for c in range(0, len(board[0])):
                boxi = (r//3)*3 + (c//3)
                if board[r][c] == ".":
                    continue 
                if board[r][c] in column[c]:
                    return False
                elif board[r][c] in row[r]:
                    return False
                elif board[r][c] in square[boxi]:
                    return False
                else:
                    column[c].add(board[r][c])
                    row[r].add(board[r][c])
                    square[boxi].add(board[r][c])
        return True