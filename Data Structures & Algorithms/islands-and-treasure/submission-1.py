class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        visit = set()
        q = deque()

        row = len(grid)
        col = len(grid[0])

        def bfs(r, c):

            if (
                r < 0 or c < 0 or
                r >= row or c >= col or
                grid[r][c] == -1 or
                (r, c) in visit
            ):
                return

            q.append((r, c))
            visit.add((r, c))

        d = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visit.add((i, j))

        while q:

            for i in range(len(q)):

                r, c = q.popleft()

                grid[r][c] = d

                bfs(r, c + 1)
                bfs(r + 1, c)
                bfs(r - 1, c)
                bfs(r, c - 1)

            d += 1