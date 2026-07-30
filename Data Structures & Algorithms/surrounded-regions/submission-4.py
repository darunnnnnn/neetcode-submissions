class Solution:
    def solve(self, board: List[List[str]]) -> None:

        row = len(board)
        col = len(board[0])

        def dfs(r, c):

            if (
                r < 0 or c < 0 or
                r >= row or c >= col or
                board[r][c] != "O"
            ):
                return

            board[r][c] = "T"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Traverse left and right boundaries
        for i in range(row):
            if board[i][0] == "O":
                dfs(i, 0)

            if board[i][col - 1] == "O":
                dfs(i, col - 1)

        # Traverse top and bottom boundaries
        for j in range(col):
            if board[0][j] == "O":
                dfs(0, j)

            if board[row - 1][j] == "O":
                dfs(row - 1, j)

        # Convert remaining O's to X and T's back to O
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"