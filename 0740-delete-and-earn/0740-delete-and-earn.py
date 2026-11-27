class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        mx=max(nums)

        arr=[0 for _ in range(mx+1)]

        for i in nums:
            arr[i]+=i

        n=len(arr)

        prev2=0
        prev1=0

        for i in range(n-1,-1,-1):
            curr = max(prev1,arr[i]+prev2)
            prev2=prev1
            prev1=curr

        return prev1                  