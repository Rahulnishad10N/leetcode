class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        m=len(image)
        n=len(image[0])
        org=image[sr][sc]
        if org == color:
            return image

        def dfs(image,sr,sc,org,color):
            if sr<0 or sr>=m or sc<0 or sc>=n:
                return

            if image[sr][sc]!=org:
                return

            image[sr][sc]=color

            dir=[(-1,0),(1,0),(0,1),(0,-1)]

            for i,j in dir:
                nr=sr+i
                nc=sc+j
                dfs(image,nr,nc,org,color)

        dfs(image,sr,sc,org,color)
        return image