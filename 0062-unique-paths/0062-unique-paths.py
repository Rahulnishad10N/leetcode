class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[0 for _ in range(n)]

        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[j]=1
                else:
                    up=0
                    left=0
                    if i>0:
                        up=dp[j]
                    if j>0:
                        left=dp[j-1]
                    dp[j]=(up+left)

        return  dp[n-1]              