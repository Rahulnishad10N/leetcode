class Solution:
    def frequencySort(self, s: str) -> str:
        mp={}

        for i in s:
            mp[i]=mp.get(i,0)+1

        heap=[]

        for elem,freq in mp.items():
            heapq.heappush(heap,(-freq,elem))

        ans=[]
        while heap:
            freq,elem=heapq.heappop(heap)
            freq*=-1
            while freq:
                ans.append(elem)
                freq-=1 

        return "".join(ans)      


        