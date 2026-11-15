class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        if n==1:
                return nums[0]
        if n==2:
            return max(nums[0],nums[1])

        a=nums[0]
        b=max(nums[0],nums[1])

        for j in range(2,n):
            pick=nums[j]+a
            notpick=b
            c=max(pick,notpick)
            a=b
            b=c

        return c      
        

 
        