class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap=[]

        for i,j in points:
            dissquare=i*i+j*j
            heapq.heappush(heap,(-dissquare,[i,j]))
            if len(heap)>k:
                heapq.heappop(heap)

        ans=[]

        while heap:
            d,e=heapq.heappop(heap)
            ans.append(e)

        return ans        
        