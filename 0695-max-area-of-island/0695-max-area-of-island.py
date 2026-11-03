class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=[[False for _ in range(n)] for _ in range(m)]

        def dfs(grid,sr,sc,visited,m,n):
            if sr<0 or sr>=m or sc<0 or sc>=n:
                return 0
            if not grid[sr][sc]:
                return 0

            if visited[sr][sc]:
                return 0

            visited[sr][sc]=True
            ans=1
            dir=[(-1,0),(1,0),(0,-1),(0,1)]

            for i,j in dir:
                nr=sr+i
                nc=sc+j
                ans+=dfs(grid,nr,nc,visited,m,n)

            return ans

        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and not visited[i][j]:
                    ans=max(ans,dfs(grid,i,j,visited,m,n))

        return ans            