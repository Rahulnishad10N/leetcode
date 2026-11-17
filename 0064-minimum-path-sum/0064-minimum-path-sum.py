class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[0 for _ in range(n)]

        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[j]=grid[i][j]
                else:
                    up=float('inf')
                    left=float('inf')
                    if i>0:
                         up=grid[i][j]+dp[j]
                    if j>0:
                        left=grid[i][j]+dp[j-1]
                    dp[j]=min(up,left)

        return dp[n-1]             
        