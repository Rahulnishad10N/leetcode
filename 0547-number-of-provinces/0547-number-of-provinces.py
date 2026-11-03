class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited=[False for _ in range(n)]

        def dfs(graph,src,visited,n):

            visited[src]=True

            for neighbour in range(n):
                if graph[src][neighbour] and not visited[neighbour]:
                    dfs(graph,neighbour,visited,n)

        
        ans=0
        for i in range(n):
            if not visited[i]:
                ans+=1
                dfs(isConnected,i,visited,n)


        return ans        
        
        