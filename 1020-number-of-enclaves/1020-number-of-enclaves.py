class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=[[False for _ in range(n)] for _ in range(m)]
        def solve(grid,sr,sc,visited,m,n):
            if sr<0 or sr>=m or sc<0 or sc>=n:
                return
            if not grid[sr][sc]:
                return    
            if visited[sr][sc]:
                return 

            visited[sr][sc]=True

            dir=[(-1,0),(1,0),(0,1),(0,-1)]

            for i,j in dir:
                nr=sr+i
                nc=sc+j
                solve(grid,nr,nc,visited,m,n)

        for i in range(n):
            if grid[0][i] and not visited[0][i]:
                solve(grid,0,i,visited,m,n)
            if grid[m-1][i] and not visited[m-1][i]:
                solve(grid,m-1,i,visited,m,n)

        for i in range(m):
            if grid[i][0] and not visited[i][0]:
                solve(grid,i,0,visited,m,n)
            if grid[i][n-1] and not visited[i][n-1]:
                solve(grid,i,n-1,visited,m,n)

        ans=0

        for i in range(m):
            for j in range(n):
                if grid[i][j] and not visited[i][j]:
                    ans+=1

        return ans                                                
        