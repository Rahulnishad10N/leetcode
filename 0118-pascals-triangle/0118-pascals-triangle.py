class Solution:
    def generate(self, rowIndex: int) -> list[list[int]]:
        
        if rowIndex==1:
            return [[1]]

        if rowIndex==2:
            return [[1],[1,1]]
        
        ans=[[1],[1,1]]
        row=[1,1]    

        for i in range(3,rowIndex+1):
            n=len(row)
            for j in range(n-1,0,-1):
                row[j]=row[j]+row[j-1]

            row.append(1)
            ans.append(row.copy())  

        return ans
        