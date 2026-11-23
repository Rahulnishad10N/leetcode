class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        n=len(nums)
        nums.sort()
        i=n-3

        ans=0

        while i>=0:
            if nums[i]+nums[i+1]>nums[i+2]:
                s=nums[i]+nums[i+1]+nums[i+2]
                ans=max(ans,s)

            i-=1

        return ans        

        