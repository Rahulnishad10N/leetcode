class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:

        n=len(triangle)
        dp=[0 for _ in range(n)]

        for i in range(n):
            dp[i]=triangle[n-1][i]

        for i in range(n-2,-1,-1):
            for j in range(i+1):
                down=triangle[i][j]+dp[j]   
                daigonal=triangle[i][j]+dp[j+1]
                dp[j]=min(down,daigonal)    
           

        return dp[0]       
        