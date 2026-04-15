class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        square = {}
        
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == '.':
                    continue
                
                if r not in row:
                    row[r] = set()
                if c not in col:
                    col[c] = set()
                if (r // 3, c // 3) not in square:
                    square[r // 3 , c // 3] = set()
                
                if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in square[(r // 3, c // 3)]:
                    return False
                
                row[r].add(board[r][c]) 
                col[c].add(board[r][c])
                square[r // 3, c // 3].add(board[r][c])
        return True        
