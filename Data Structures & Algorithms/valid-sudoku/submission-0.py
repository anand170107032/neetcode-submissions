class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        # rows
        for r in range(n):
            seen = set()
            for c in range(n):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in seen:
                    return False
                else:
                    seen.add(board[r][c])

        # columns
        for c in range(n):
            seen = set()
            for r in range(n):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in seen:
                    return False
                else:
                    seen.add(board[r][c])

        # squares
        for r in range(0, n, 3):
            for c in range(0, n, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        if board[r+i][c+j] == ".":
                            continue
                        elif board[r+i][c+j] in seen:
                            return False
                        else:
                            seen.add(board[r+i][c+j])

        return True