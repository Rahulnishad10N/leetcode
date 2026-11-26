class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        n=len(points)
        points.sort(key=lambda x: x[0])

        start=points[0][0]
        end=points[0][1]
        ans=0

        for i in range(1,n):
            if start<=points[i][1] and points[i][0]<=end:
                start=max(start,points[i][0])
                end=min(end,points[i][1])
            else:
                ans+=1
                start=points[i][0]
                end=points[i][1]

        return ans+1           