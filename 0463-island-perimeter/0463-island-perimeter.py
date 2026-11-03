class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:

        def dfs(grid,sr,sc,visited,m,n):
            if sr<0 or sr>=m or sc<0 or sc>=n:
                return 1
            if not grid[sr][sc]:
                return 1

            if visited[sr][sc]:
                return 0

            visited[sr][sc]=True
            ans=0
            dir=[(-1,0),(1,0),(0,-1),(0,1)]

            for i,j in dir:
                nr=sr+i
                nc=sc+j
                ans+=dfs(grid,nr,nc,visited,m,n)

            return ans

        m=len(grid)
        n=len(grid[0])
        visited=[[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    return dfs(grid,i,j,visited,m,n)       

        