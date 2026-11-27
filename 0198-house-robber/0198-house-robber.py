class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        dp=[0 for _ in range(n+2)]
        prev2=0
        prev1=0

        for i in range(n-1,-1,-1):
            notRob=prev1
            Rob=nums[i]+prev2
            curr= max(notRob,Rob)
            prev2=prev1
            prev1=curr

        return curr       
              
        

 
        