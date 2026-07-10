class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])

        q = deque()
        visit = set()

        t = 0

        def bfs(r, c):

            if (
                r < 0 or c < 0 or
                r >= row or c >= col or
                grid[r][c] == 0 or
                (r, c) in visit or
                grid[r][c] == 2
            ):
                return

            grid[r][c] = 2
            visit.add((r, c))
            q.append((r, c))

        for i in range(row):
            for j in range(col):

                if grid[i][j] == 2:
                    q.append((i, j))
                    visit.add((i, j))

        while q:

            changed = False

            for _ in range(len(q)):

                r, c = q.popleft()

                before = len(q)

                bfs(r + 1, c)
                bfs(r - 1, c)
                bfs(r, c + 1)
                bfs(r, c - 1)

                if len(q) > before:
                    changed = True

            if changed:
                t += 1

        for r in grid:
            if 1 in r:
                return -1

        return t