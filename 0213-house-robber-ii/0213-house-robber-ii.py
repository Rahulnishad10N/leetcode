class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        if n==0:
            return 0

        if n==1:
            return nums[0]    

        def solve(i,j,nums):


            if j==i:
                return nums[i]

            if j==i+1:
                return max(nums[i],nums[i+1])

            a=nums[i]
            b=max(nums[i],nums[i+1])    

            for r in range(i+2,j+1):
                pick=nums[r]+a
                notpick=b
                c=max(pick,notpick)
                a=b
                b=c
            return c

        return max(solve(0,n-2,nums),solve(1,n-1,nums))                    
        