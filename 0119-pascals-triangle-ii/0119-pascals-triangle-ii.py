class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex==0:
            return [1]

        if rowIndex==1:
            return [1,1]

        row=[1,1]    

        for i in range(2,rowIndex+1):
            n=len(row)
            for j in range(n-1,0,-1):
                row[j]=row[j]+row[j-1]

            row.append(1)  

        return row
        