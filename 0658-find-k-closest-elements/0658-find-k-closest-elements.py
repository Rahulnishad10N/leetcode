class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap=[]

        for i in arr:
            dist=abs(x-i)
            heapq.heappush(heap,(-dist,-i))
            if len(heap)>k:
                heapq.heappop(heap)

        ans=[]

        while heap:
            d,e=heapq.heappop(heap)
            ans.append(-e)
        ans.sort()
        return ans             
        