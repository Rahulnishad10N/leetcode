class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)

        if n==1:
            return nums[0]

        ## 0 to n-2

        prev2=0
        prev1=0

        for i in range(n-2,-1,-1):
            notRob=prev1
            Rob=nums[i]+prev2
            curr1= max(notRob,Rob)
            prev2=prev1
            prev1=curr1

        prev2=0
        prev1=0


        for i in range(n-1,0,-1):
            notRob=prev1
            Rob=nums[i]+prev2
            curr2= max(notRob,Rob)
            prev2=prev1
            prev1=curr2


        return max(curr1,curr2)       
        