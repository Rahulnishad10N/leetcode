class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        n=len(nums)
        heap=[]

        for i in nums:
            heapq.heappush(heap,i)

            if len(heap)>k:
                heapq.heappop(heap)

        return heap[0]        
        