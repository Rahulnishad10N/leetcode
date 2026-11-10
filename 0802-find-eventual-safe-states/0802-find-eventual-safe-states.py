class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:

        n=len(graph)
        visited=[False for _ in range(n)]
        path=[False for _ in range(n)]
        check=[False for _ in range(n)]

        def dfs(adj,src,visited,path,check):
            visited[src]=True
            path[src]=True

            for neighbour in adj[src]:
                if not visited[neighbour]:
                    if dfs(adj,neighbour,visited,path,check):
                        return True

                elif path[neighbour]:
                    return True
            path[src]=False        
            check[src]=True
            return False

        for i in range(n):
            if not visited[i]:
                dfs(graph,i,visited,path,check)

        ans=[]

        for i in range(n):
            if check[i]:
                ans.append(i)

        return ans                                    
        