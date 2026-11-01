class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        adj=[[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited=[False for _ in range(n)]
        def check(adj,src,visited,dest):
            visited[src]=True
            if src==dest:
                return True

            for neighbour in adj[src]:
                if not visited[neighbour]:
                    if check(adj,neighbour,visited,dest):
                        return True

            return False

        return check(adj,source,visited,destination)    