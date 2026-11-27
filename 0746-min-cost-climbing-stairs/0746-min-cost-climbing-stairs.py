class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n=len(cost)

        prev2=0
        prev1=0

        for i in range(n-1,-1,-1):
            curr= cost[i]+min(prev1,prev2)
            prev2=prev1
            prev1=curr


        return min(prev1,prev2)       
        