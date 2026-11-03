class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(sr, sc):
            if sr < 0 or sr >= m or sc < 0 or sc >= n:
                return False

            if grid[sr][sc] == 1:
                return True

            grid[sr][sc] = 1

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            ans = True

            for i, j in directions:
                nr = sr + i
                nc = sc + j

                result = dfs(nr, nc)
                ans = ans and result

            return ans

        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if dfs(i, j):
                        count += 1

        return count