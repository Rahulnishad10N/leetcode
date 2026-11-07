class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        adj=[[] for _ in range(n+1)]
        for i in dislikes:
            a=i[0]
            b=i[1]
            adj[a].append(b)
            adj[b].append(a)
        color=[-1 for _ in range(n+1)]

        def dfs(adj,src,color):
            for neighbour in adj[src]:
                if color[neighbour]==-1:
                    if color[src]==0:
                        color[neighbour]=1
                    else:
                        color[neighbour]=0
                    if not dfs(adj,neighbour,color):
                        return False
                elif color[neighbour]==color[src]:
                    return False
            return True

        for i in range(n):
            if color[i]==-1:
                color[i]=0
                if not dfs(adj,i,color):
                    return False

        return True