class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        n=len(firstList)
        m=len(secondList)
        ans=[]

        i=0
        j=0

        while i<n and j<m:
            if firstList[i][0]<=secondList[j][1] and secondList[j][0]<=firstList[i][1]:
                ans.append([max(firstList[i][0],secondList[j][0]),min(secondList[j][1],firstList[i][1])])

            if firstList[i][1]<=secondList[j][1]:
                i+=1
            else:
                j+=1

        return ans        

        