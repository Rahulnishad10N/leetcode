class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])

        row=[0 for _ in range(m)]
        col=[0 for _ in range(n)]

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    row[i]+=1
                    col[j]+=1

        ans=0

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if row[i]>1 or col[j]>1:
                        ans+=1

        return ans                           
        