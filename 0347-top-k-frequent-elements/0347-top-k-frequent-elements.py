class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        n=len(nums)
        mp={}

        for i in nums:
            mp[i]=mp.get(i,0)+1

        heap=[]

        for e , f in mp.items():
            heapq.heappush(heap,(f,e))
            if len(heap)>k:
                heapq.heappop(heap)

        ans=[]

        while heap:
            f,e=heapq.heappop(heap)
            ans.append(e)   

        return ans         
            

        