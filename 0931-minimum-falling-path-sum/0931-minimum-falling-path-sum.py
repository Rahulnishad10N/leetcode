class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:

        m = len(matrix)
        n = len(matrix[0])
        prev= [0 for _ in range(n)]

        for i in range(m):
            curr= [0 for _ in range(n)]

            for j in range(n):
                if i == 0:
                    curr[j] = matrix[i][j]
                else:
                    up = float('inf')
                    upleft = float('inf')
                    upright = float('inf')

                    up = matrix[i][j] + prev[j]

                    if j-1 >= 0:
                        upleft = matrix[i][j] + prev[j-1]

                    if j+1 < n:
                        upright = matrix[i][j] + prev[j+1]

                    curr[j] = min(up, min(upleft, upright))
            prev=curr        

        ans = float('inf')

        for i in range(n):
            ans = min(ans, prev[i])

        return ans