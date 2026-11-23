class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1],reverse=True)
        
        ans=0
        for i,j in  boxTypes:
            
            while i and truckSize:
                ans+=j
                i-=1
                truckSize-=1

        return ans        
        
        