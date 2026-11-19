class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total=sum(nums)
        if total%2:
            return False


        def isSubsetSum(arr,target):
            n=len(arr)
            prev=[False for _ in range(target+1)]

            prev[0]=True

            if arr[0]<=target:
                prev[arr[0]]=True

            for i in range(1,n):
                for j in range(target,0,-1):
                    notPick=prev[j]
                    pick=False
                    if arr[i]<=j:
                        pick=prev[j-arr[i]]
                    
                    prev[j]=pick or notPick
                
            return prev[target]

        return isSubsetSum(nums,total//2)