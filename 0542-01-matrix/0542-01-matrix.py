class Solution:
    def updateMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        m=len(grid)
        n=len(grid[0])

        visited=[[False for _ in range(n)] for _ in range(m)]
        q=deque()

        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    q.append((i,j,0))
                    visited[i][j]=True

        dir=[(-1,0),(1,0),(0,1),(0,-1)]            

        while q:
            r,c,d=q.popleft()

            grid[r][c]=d

            for i,j in dir:
                nr=r+i
                nc=c+j
                if 0<=nr<m and 0<=nc<n and not visited[nr][nc] and grid[nr][nc]:
                    visited[nr][nc]=True
                    q.append((nr,nc,d+1))

        return grid

        