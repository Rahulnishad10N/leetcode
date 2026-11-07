class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])

        fresh=0
        q=deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j,0))
                if grid[i][j]==1:
                    fresh+=1    
        
        tx=0
        dir=[(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            size=len(q)

            for i in range(size):
                r,c,t=q.popleft()
                tx=max(tx,t)

                for i , j in dir:
                    nr=r+i
                    nc=c+j
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        q.append((nr,nc,t+1))
                        fresh-=1

        if fresh==0:
            return tx

        return -1                    

                
