class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])
        visited=[[False for _ in range(n)] for _ in range(m)]

        def dfs(board,sr,sc,visited,m,n):
            if sr<0 or sr>=m or sc<0 or sc>=n:
                return
            if board[sr][sc]=="X":
                return
            if visited[sr][sc]:
                return

            visited[sr][sc]=True
            dir=[(-1,0),(1,0),(0,1),(0,-1)]

            for i , j in dir:
                nr=sr+i
                nc=sc+j

                dfs(board,nr,nc,visited,m,n)


        for i in range(n):
            if board[0][i]=="O" and not visited[0][i]:
                dfs(board,0,i,visited,m,n) 
            if board[m-1][i]=="O" and not visited[m-1][i]:
                dfs(board,m-1,i,visited,m,n)

        for i in range(m):
            if board[i][0]=="O" and not visited[i][0]:
                dfs(board,i,0,visited,m,n)
            if board[i][n-1]=="O" and not visited[i][n-1]:
                dfs(board,i,n-1,visited,m,n)


        for i in range(m):
            for j in range(n):
                if board[i][j]=="O" and not visited[i][j]:
                    board[i][j]="X"             
            
        