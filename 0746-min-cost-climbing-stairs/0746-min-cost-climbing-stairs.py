class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n=len(cost)

        if n==0 or n==1:
                return 0

        prev2=0
        prev1=0        
        for i in range(2,n+1):
            curr= min(cost[i-1]+prev1,cost[i-2]+prev2)
            prev2=prev1
            prev1=curr

        return curr       
        