class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        n=len(intervals)
        intervals.sort(key=lambda x: x[0])
        start=intervals[0][0]
        end=intervals[0][1]

        ans=[]

        for i in range(1,n):
            if start<=intervals[i][1] and intervals[i][0]<=end:
                end=max(end,intervals[i][1])

            else:
                ans.append([start,end])
                start=intervals[i][0]    
                end=intervals[i][1] 

        ans.append([start,end])           

        return ans        
        