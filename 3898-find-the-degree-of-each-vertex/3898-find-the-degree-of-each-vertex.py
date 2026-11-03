class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n=len(matrix)
        ans=[0 for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if matrix[i][j]:
                    ans[i]+=1

        return ans            

        