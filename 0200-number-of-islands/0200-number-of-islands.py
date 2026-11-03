class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=[[False for _ in range(n)] for _ in range(m)]
        def dfs(grid,sr,sc,visited,m,n):
            if sr<0 or sr>=m or sc<0 or sc>=n:
                return 
            if grid[sr][sc]=="0":
                return 

            if visited[sr][sc]:
                return 

            visited[sr][sc]=True
            dir=[(-1,0),(1,0),(0,-1),(0,1)]

            for i,j in dir:
                nr=sr+i
                nc=sc+j
                dfs(grid,nr,nc,visited,m,n)

        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and not visited[i][j]:
                    ans+=1
                    dfs(grid,i,j,visited,m,n) 
        
        return ans

        